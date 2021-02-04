from django.shortcuts import render
from django.conf import settings

from .models import BillingAddress
from motorhomes.models import Motorhome
# A Checkout view


def CheckoutView(request):
    user=request.user
    if BillingAddress.objects.filter(user=user):
        billingaddress = BillingAddress.objects.get(user=user)

    motorhome = Motorhome.objects.get(pk=1)
    context = {
        'billingaddress': billingaddress,
        'motorhome': motorhome,
    }

    return render(request, 'checkout/checkout.html', context)
