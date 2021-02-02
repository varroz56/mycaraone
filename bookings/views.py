from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Booking
from .forms import BookingForm

# a view to show all bookings


def BookingListView(request):
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
    }
    return render(request, 'bookings/bookings_list.html', context)


# A view to create Booking
class BookingView(CreateView):
    model = Booking
    template_name = 'bookings/create_booking.html'
    fields = '__all__'
    success_url = reverse_lazy('create_booking')

# a view to show the availabilty form


def MotorhomeFilterView(request):
    return render(request, 'bookings/motorhome_filter.html')
