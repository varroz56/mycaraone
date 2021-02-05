from django.urls import path
from .views import CheckoutView, CheckoutSuccessView


urlpatterns = [
    path('', CheckoutView, name='checkout'),
    path('success/', CheckoutSuccessView, name='checkout_success'),
]
