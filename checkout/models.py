from django.db import models
from django.contrib.auth.models import User
from bookings.models import Booking

# uuid to create ref for booking summary
import uuid
# Billing address


class BillingAddress(models.Model):

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=15)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} - {self.user}"


class BookingSummary(models.Model):
    """ This model stores the details of the booking and transaction"""
    # using UUID to create booking refrence number
    booking_reference = models.CharField(
        max_length=32, null=False, editable=False)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=15)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=255)

    date_created = models.DateTimeField(auto_now_add=True)

    booking_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
    def create_booking_ref(self):
        # create ref using uuid
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        # if not set, create booking ref
        if not self.booking_reference:
            self.booking_reference = self.create_booking_ref()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_reference
