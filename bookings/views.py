from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .models import Booking
from .forms import BookingForm

from motorhomes.models import Motorhome

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

# a view to create booking with a choosen vehicle


def BookThisMotorhome(request, pk):
    """ This view is to create a booking after choosing motorhome """

    user = request.user
    template = 'bookings/book_this_motorhome.html'
    motorhome = get_object_or_404(Motorhome, pk=pk)

    context = {
        'motorhome': motorhome,
    }
    return render(request, template, context)
