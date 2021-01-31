from django.forms import ModelForm

from .models import Booking

# A simple model form to create booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
