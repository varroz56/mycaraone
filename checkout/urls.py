from django.urls import path
from .views import CheckoutView


urlpatterns = [
    path('', CheckoutView, name='checkout'),
]
