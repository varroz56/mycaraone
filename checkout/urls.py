from django.urls import path
from .views import CheckoutView, CheckoutSuccessView
from .webhooks import webhook

urlpatterns = [
    path('', CheckoutView, name='checkout'),
    path('success/', CheckoutSuccessView, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]
