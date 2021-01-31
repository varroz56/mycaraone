from django.shortcuts import render
# A Checkout view


def CheckoutView(request):
    return render(request, 'checkout/checkout.html')
