from django.urls import path

from .views import MotorhomeListView, MotorhomeDetailedView

urlpatterns = [
    path('', MotorhomeListView, name='motorhomes'),
    path('details/<int:pk>', MotorhomeDetailedView, name='motorhome_details'),
]
