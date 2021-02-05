from django.shortcuts import render
from django.conf import settings

from .models import BillingAddress
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

    # get vars from session
    mid = request.session['motorhome.pk']
    uid = request.session['user.pk']
    days = request.session['days']
    total = request.session['total']
    booked_from = request.session['booked_from']
    booked_until = request.session['booked_until']

    # set reverse url
    reverse_url = ('/bookings/book_this_motorhome/' + str(mid))
    # if request.method=='POST':
    user = request.user

    if user.id != uid:
        messages.add_message(
            request, messages.ERROR, 'Sorry, We were unable render the checkout page, please try again or contact us')

        return render(reverse_url)

    else:
        # using stripe inbuilt methods
        # stripe total 
        stripe_total = (int(total)*100)

        # passing the secret key to stripe
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
