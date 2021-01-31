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

    def __init__(self, *srgs, **kwargs):
        """ Placeholders for the formfields"""
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number':'Phone Number',
            'address_line1':'Address Line 1',
            'address_line2':'Address Line 2',
            'postcode':'Postcode',
            'city':'City',
            'country':'Country',
        }
        # https://docs.djangoproject.com/en/3.1/ref/forms/widgets/
        # Set autofocus on the name
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'billing-address-field'
            self.fields[field].required = True
            self.fields[field].label = False
