from django import forms
from django.forms import ModelForm
from .models import UserProfile

# A form to handle the user profile view,
# in this way excluded all non-createable or changeable
# fields and will be able to handle create read update


class UserProfileViewForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'profile_picture']
