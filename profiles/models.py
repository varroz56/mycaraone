from django.db import models
from django.contrib.auth.models import User


# Set deafult path for uploaded user profile pictures
# https://docs.djangoproject.com/en/3.1/ref/models/fields/
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images/profile_picture/user_<id>/<filename>
    return 'images/profile_pictures/user_{0}/{1}'.format(instance.user.id, filename)


# User Profile stores User related not billing address information


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(
        default='images/profile_pictures/userlight.png', upload_to=user_directory_path, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
