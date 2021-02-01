from django.db import models


# Manufacturer model stores basic information about the manufacturer
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Vehicle stores information about the caravan/van


class Vehicle(models.Model):
    make = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.model


# Set deafult path for uploaded motorhome pictures
# https://docs.djangoproject.com/en/3.1/ref/models/fields/
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images/motorhome_picture/motorhome_<id>/<filename>
    return 'images/motorhome_pictures/{0}'.format(filename)
# Motorhome model


# Motorhome stores the information about the rented Motorhomes
class Motorhome(models.Model):

    class PremiumChoices(models.TextChoices):
        BASIC = 'Basic',
        COMFORT = 'Comfort',
        PREMIUM = 'Premium',

    class GroupChoices(models.TextChoices):
        SINGLE = 'Single',
        COUPLE = 'Couple',
        FAMILY = 'Family'

    nickname = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    seats = models.IntegerField(default=2)
    persons_to_sleep = models.IntegerField(default=2)
    number_of_double_beds = models.IntegerField(default=0)
    category = models.CharField(
        max_length=50,
        choices=PremiumChoices.choices,
        default=PremiumChoices.COMFORT
    )
    good_for_groups = models.CharField(
        max_length=50,
        choices=GroupChoices.choices,
        default=GroupChoices.COUPLE
    )
    picture1 = models.ImageField(upload_to=user_directory_path)
    picture2 = models.ImageField(upload_to=user_directory_path)
    picture3 = models.ImageField(upload_to=user_directory_path)
    picture4 = models.ImageField(upload_to=user_directory_path)
    picture5 = models.ImageField(upload_to=user_directory_path)

    artricle1=models.TextField(null=True, blank=True)
    artricle2=models.TextField(null=True, blank=True)
    artricle3=models.TextField(null=True, blank=True)
    artricle4=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nickname
