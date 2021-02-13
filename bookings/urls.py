from django.urls import path

from .views import BookingListView, BookingView, BookThisMotorhome, MyBookings, CheckoutThisBooking

urlpatterns = [
    path('all/', BookingListView, name='allbookings'),
    path('my_bookings/', MyBookings, name='mybookings'),
    path('create_booking/', BookingView.as_view(), name='create_booking'),
    path('book_this_motorhome/<int:pk>',
         BookThisMotorhome, name='book_this_motorhome'),
    path('finish_booking/<int:pk>', CheckoutThisBooking, name='finish_booking'),
]
