from django.http import HttpResponse

from .models import BookingSummary

import time


class StripeWH_Handler:
    """ Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment_intent.payment_succeeded event 
            if the payment or the booking interrupted, 
            this will delay a bit and create or update the booking summary

            also, adding pid to bookingsummary
        """
        intent = event.data.object
        intent = intent.id
        pid = intent.id

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        # stripe total amount back to "normal"
        booking_total = round(intent.charges.data[0].amount / 100, 2)

        # check wether value was provided to the given form field
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # checking if the bookingsummary was successfully created or it was interrupted
        # applying delay to avoid mistakenly duplicated bookings
        bookingsummary_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                bookingsummary = BookingSummary.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    address_line1__iexact=shipping_details.address.line1,
                    address_line2__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    country__iexact=shipping_details.address.country,
                    booking_total=booking_total,
                    stripe_pid=pid,
                )
                bookingsummary_exists = True
                break
            except BookingSummary.DoesNotExist:
                # delaying the re-check
                attempt += 1
                time.sleep(1)
        # The bookingsummary exists 
        if bookingsummary_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Bookingsummary already saved, the payment verified',
                status=200)
        else:
            bookingsummary = None
            try:
                bookingsummary = BookingSummary.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    address_line1=shipping_details.address.line1,
                    address_line2=shipping_details.address.line2,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    country=shipping_details.address.country,
                    booking_total=booking_total,
                    stripe_pid=pid,
                )
            # anything happens, rais a server error
            except Exception as e:
                if bookingsummary:
                    bookingsummary.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=404)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created bookingsummary in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """ Handle payment_intent.payment_failed event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
