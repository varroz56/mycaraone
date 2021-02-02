from django.urls import path

from .views import BookingListView, BookingView, MotorhomeFilterView

urlpatterns = [
    path('all/', BookingListView, name='allbookings'),
    path('create_booking/', BookingView.as_view(), name='create_booking'),
    path('search/', MotorhomeFilterView, name="motorhome_filter"),
]
