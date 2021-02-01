from django.urls import path
from .views import IndexView, ContactFormView


urlpatterns = [
    path('', IndexView, name='index'),
    path('contact_us/', ContactFormView, name='contact_us_message'),
]
