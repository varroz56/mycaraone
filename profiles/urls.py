from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path('myprofile/', UserProfileView, name='user_profile'),
]
