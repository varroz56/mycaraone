from django import forms
from django.forms import ModelForm
from .models import UserProfile

from checkout.models import BillingAddress
# A form to handle the user profile view,
# in this way excluded all non-createable or changeable
# fields and will be able to handle create read update


class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'profile_picture']


# Billing address form

class BillingAddressForm(ModelForm):
    class Meta:
        model = BillingAddress
        exclude = ['user']
