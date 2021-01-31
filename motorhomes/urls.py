from django.urls import path

from .views import MotorhomeListView

urlpatterns = [
    path('', MotorhomeListView, name='motorhomes'),
]
