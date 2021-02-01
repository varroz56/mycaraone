from django.urls import path
from .views import UserProfileView, UserProfileUpdateView


urlpatterns = [
    path('myprofile/', UserProfileView, name='myprofile'),
    path('myprofile/update/', UserProfileUpdateView, name='update_myprofile'),

]
