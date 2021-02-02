from datetime import date, timedelta
from django import forms
from django.forms import ModelForm

from .models import Booking

# A simple model form to create booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


# a form to filter Motorhomes

class MotorhomeFilterForm(forms.Form):
    """ This is to filter motorhomes for the given dates
        Required seats
        Required berths
        and daily rebntal fee
    """
    PREMIUM_CHOICES = (
        ("BASIC", 'Basic'),
        ("COMFORT", 'Comfort'),
        ('PREMIUM', 'Premium'),
    )

    GROUP_CHOICES = (
        ("SINGLE", 'Single'),
        ("COUPLE", 'Couple'),
        ("FAMILY", 'Family'),
    )

    RENTAL_FEE_CHOICES = (
        ("UNDER100", "Under 100"),
        ("UNDER150", "Under 150"),
        ("UNDER200", "Under 200"),
        ("200ABOVE", "200 and above"),
    )

    start_date = forms.DateField(initial=date.today())
    end_date = forms.DateField(initial=date.today() + timedelta(days=1))

    required_seats = forms.NumberInput()
    required_berths = forms.NumberInput()

    premium_choices = forms.ChoiceField(
        choices=PREMIUM_CHOICES
    )

    group_size_choices = forms.ChoiceField(
        choices=GROUP_CHOICES)
    daily_rental_fee = forms.ChoiceField(
        choices=RENTAL_FEE_CHOICES)
