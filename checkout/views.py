from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.conf import settings

from .models import BillingAddress, BookingSummary
from bookings.models import Booking
from motorhomes.models import Motorhome
# https://stripe.com/docs/payments/accept-a-payment?integration=elements
# https://github.com/stripe-samples/accept-a-card-payment/blob/master/using-webhooks/server/python/server.py#L43-L46
# CodeInstitute checkout app
import stripe
import json
from django.contrib import messages

import dateutil
from dateutil.parser import parse
# A Checkout view


def CheckoutView(request):
    """ This view to take payment and confirm booking for customer"""
    # stripe api keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    user = request.user
    # get vars from session
    mid = request.session['motorhome.pk']
    uid = request.session['user.pk']
    days = request.session['days']
    total = request.session['total']
    booked_from = request.session['booked_from']
    booked_until = request.session['booked_until']
    booking_id = request.session['booking_id']

    if request.method == 'POST':
        try:
            # getting checkout data
            full_name = request.POST.get('full_name', False),
            email = request.POST.get('email', False),
            phone_number = request.POST.get('phone_number', False),
            address_line1 = request.POST.get('street_number', False),
            address_line2 = request.POST.get('route', False),
            postcode = request.POST.get('postal_code', False),
            city = request.POST.get('locality', False),
            country = request.POST.get('country', False),

            bookingsummary = BookingSummary(
                user=user,
                booking=Booking.objects.get(booking_id=booking_id),
                full_name=full_name[0],
                email=email[0],
                phone_number=phone_number[0],
                address_line1=address_line1[0],
                address_line2=address_line2[0],
                postcode=postcode[0],
                city=city[0],
                country=country[0],
                booking_total=total,
            )
            bookingsummary.save()
            request.session['booking_reference'] = bookingsummary.booking_reference
            messages.add_message(request, messages.SUCCESS, 'Checkout Success')
            return redirect(reverse(CheckoutSuccessView))

        except:
            messages.add_message(
                request, messages.ERROR, 'Something went wrong, please try again or contact us')
        return redirect(reverse(CheckoutView))
    else:

        # using stripe inbuilt methods
        # stripe total
        stripe_total = (int(total)*100)
        stripe.api_key = stripe_secret_key
        # creating payment intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        motorhome = Motorhome.objects.get(pk=mid)

        if BillingAddress.objects.filter(user=user):
            billingaddress = BillingAddress.objects.get(user=user)

            context = {
                'days': days,
                'total': total,
                'booked_from': dateutil.parser.parse(booked_from),
                'booked_until': dateutil.parser.parse(booked_until),
                'billingaddress': billingaddress,
                'motorhome': motorhome,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
            }
        else:
            context = {
                'days': days,
                'total': total,
                'booked_from': dateutil.parser.parse(booked_from),
                'booked_until': dateutil.parser.parse(booked_until),
                'billingaddress': None,
                'motorhome': motorhome,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
            }
    return render(request, 'checkout/checkout.html', context)


def CheckoutSuccessView(request):
    """ Checkout Success view """
    bookingsummary = get_object_or_404(
        BookingSummary, booking_reference=request.session['booking_reference'])

    context = {
        'bookingsummary': bookingsummary
    }
    messages.add_message(
        request, messages.SUCCESS, 'Thank you, Your Booking has been confirmed and paid')
    return render(request, 'checkout/checkout_success.html', context)
