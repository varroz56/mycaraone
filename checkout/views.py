from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from .models import BillingAddress, BookingSummary
from bookings.models import Booking
from motorhomes.models import Motorhome
from profiles.models import UserProfile
# https://stripe.com/docs/payments/accept-a-payment?integration=elements
# https://github.com/stripe-samples/accept-a-card-payment/blob/master/using-webhooks/server/python/server.py#L43-L46
# CodeInstitute checkout app
import stripe
import json
from django.contrib import messages

import dateutil
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required

# cache most important checkout data


@require_POST
def CacheCheckoutDataView(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'booking_id': request.session['booking_id'],
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# A Checkout view


@login_required
def CheckoutView(request):
    """ This view to take payment and confirm booking for customer"""
    user = request.user

    if request.user.id != request.session['user.pk']:
        messages.add_message(
            request, messages.WARNING, 'User session expired please create a new booking')
        print('not this user')
        return redirect(reverse('motorhomes'))
        # get vars from session
    mid = request.session['motorhome.pk']
    days = request.session['days']
    total = request.session['total']
    booked_from = request.session['booked_from']
    booked_until = request.session['booked_until']
    booking_id = request.session['booking_id']
    # stripe api keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        try:
            # getting checkout data
            full_name = request.POST.get('full_name', False)
            email = request.POST.get('email', False)
            phone_number = request.POST.get('phone_number', False)
            address_line1 = request.POST.get('street_number', False)
            address_line2 = request.POST.get('route', False)
            postcode = request.POST.get('postal_code', False)
            city = request.POST.get('locality', False)
            country = request.POST.get('country', False)
            # accessing pid
            pid = request.POST.get('client_secret').split('_secret')[0]

            bookingsummary = BookingSummary(
                user=request.session['user.pk'],
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
                stripe_pid=pid,
            )
            bookingsummary.save()
            # set boking status to paid and confirmed
            bookingsummary.booking.status_to_paid_and_confirmed()
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
        userprofile = UserProfile.objects.get(user=request.user)
        context = {
            'days': days,
            'total': total,
            'booked_from': dateutil.parser.parse(booked_from),
            'booked_until': dateutil.parser.parse(booked_until),
            'billingaddress': billingaddress,
            'userprofile': userprofile,
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
                'userprofile': userprofile,
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
