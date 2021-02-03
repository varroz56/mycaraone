from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .models import Booking
from .forms import BookingForm, BookThisMotorhomeForm
from django.contrib import messages
from motorhomes.models import Motorhome
import dateutil
from dateutil.parser import parse

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
    form = BookThisMotorhomeForm()
    context = {
        'motorhome': motorhome,
        'form': form,
    }
    if request.method == 'POST':

        booked_from = request.POST.get('start_date', False)
        booked_until = request.POST.get('end_date', False)
        booked_until = dateutil.parser.parse(booked_until)
        booked_from = dateutil.parser.parse(booked_from)
        print(booked_from)
        try:
            booking = Booking(
                booked_by=user,
                booked_vehicle=motorhome,
                booked_from=booked_from,
                booked_until=booked_until,
            )
            booking.save()
            
            template = 'checkout/checkout.html'
            context = {
                'booking': booking,
            }
            messages.add_message(request, messages.SUCCESS,
                                 "Your Booking has been created, let's go to checkout")
            return redirect(CheckoutView, context)
        except:
            messages.add_message(request, messages.ERROR,
                                 'Sorry, We were unable to create your booking, please try again or contact us')
            return render(request, template, context)

    return render(request, template, context)
