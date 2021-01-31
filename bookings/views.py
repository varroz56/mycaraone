from django.shortcuts import render

from .models import Booking
# a view to show all bookings


def BookingListView(request):
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
    }
    return render(request, 'bookings/bookings_list.html', context)
