from django.forms import ModelForm

from .models import Booking

# A simple model form to create booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


# This the customer facing form when book from motorhome detailed page
class BookThisMotorhomeForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['booked_from', 'booked_until']
