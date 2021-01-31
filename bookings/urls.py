from django.urls import path

from .views import BookingListView

urlpatterns = [
    path('all/', BookingListView, name='allbookings'),
]
