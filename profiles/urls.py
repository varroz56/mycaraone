from django.urls import path
from .views import UserProfileView, UserProfileUpdateView, CreateBillingAddressView, UpadeBillingAddressView


urlpatterns = [
    path('myprofile/', UserProfileView, name='myprofile'),
    path('myprofile/update/', UserProfileUpdateView, name='update_myprofile'),
    path('myprofile/billing_address/create/',
         CreateBillingAddressView, name='create_billing_address'),
    path('myprofile/billing_address/update/',
         UpadeBillingAddressView, name='update_billing_address'),

]
