from django.urls import path
from .views import CheckoutView, CheckoutSuccessView, CacheCheckoutDataView, CheckoutAddressView
from .webhooks import webhook

urlpatterns = [
    path('billingaddress/', CheckoutAddressView, name='checkout_address'),
    path('', CheckoutView, name='checkout'),
    path('success/', CheckoutSuccessView, name='checkout_success'),
    path('cache_checkout_data/', CacheCheckoutDataView,
         name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
