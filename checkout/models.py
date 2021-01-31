from django.db import models
from django.contrib.auth.models import User

# Billing address


class BillingAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    postcode = models.CharField(max_length=15)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} - {self.user.username}"
