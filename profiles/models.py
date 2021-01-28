from django.db import models
from django.contrib.auth.models import User


# Set deafult path for uploaded user profile pictures
# https://docs.djangoproject.com/en/3.1/ref/models/fields/
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/profile_picture/user_{0}/{1}'.format(instance.user.id, filename)
