from django.urls import path
from .views import UserProfileView, UserProfileUpdateView, CreateBillingAddressView


urlpatterns = [
    path('myprofile/', UserProfileView, name='myprofile'),
    path('myprofile/update/', UserProfileUpdateView, name='update_myprofile'),
    path('myprofile/billing_address/create/',
         CreateBillingAddressView, name='create_billing_address')

]
