from django.shortcuts import render
from django.conf import settings

from .models import BillingAddress
from motorhomes.models import Motorhome
# https://stripe.com/docs/payments/accept-a-payment?integration=elements
# https://github.com/stripe-samples/accept-a-card-payment/blob/master/using-webhooks/server/python/server.py#L43-L46
# CodeInstitute checkout app
import stripe
import json

# A Checkout view


def CheckoutView(request):
    """ This view to take payment and confirm booking for customer"""
    # stripe api keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    print(stripe_secret_key)
    # if request.method=='POST':
    user = request.user
    motorhome = Motorhome.objects.get(pk=1)
    if BillingAddress.objects.filter(user=user):
        billingaddress = BillingAddress.objects.get(user=user)

        context = {
            'billingaddress': billingaddress,
            'motorhome': motorhome,
        }
    else:
        context = {
            'billingaddress': None,
            'motorhome': motorhome,
            'stripe_public_key': stripe_public_key,
            'client_secret': stripe_secret_key,
        }
    return render(request, 'checkout/checkout.html', context)
