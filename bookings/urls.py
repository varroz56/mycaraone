from django.urls import path

from .views import BookingListView, BookingView, BookThisMotorhome

urlpatterns = [
    path('all/', BookingListView, name='allbookings'),
    path('create_booking/', BookingView.as_view(), name='create_booking'),
    path('book_this_motorhome/<int:pk>', BookThisMotorhome, name='book_this_motorhome'),
]
