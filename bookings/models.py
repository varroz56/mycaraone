from datetime import date
from django.db import models

# uuid to create ref for booking
import uuid

from motorhomes.models import Motorhome
from django.contrib.auth.models import User
# Booking model to store booking details


class Booking(models.Model):
    """ Status choices for the booking, then the essential information about the booking"""
    class StatusChoices(models.TextChoices):
        BOOKED = 'Booked',
        PAIDBUTNOTCONFIRMED = 'Paid but not confirmed',
        CONFIRMEDBUTNOTPAID = 'Confirmed but not paid',
        PAIDANDCONFIRMED = 'Paid and Confirmed'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'

    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_vehicle = models.ForeignKey(Motorhome, on_delete=models.CASCADE)
    booked_from = models.DateField(default=date.today)
    booked_until = models.DateField(default=date.today)
    booked_on = models.DateTimeField(auto_now_add=True)

    booking_id = models.CharField(
        max_length=32, null=False, editable=False)

    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.BOOKED
    )
    closed_on = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    class Meta:
        ordering = ['booked_by', 'booked_on']

    def create_booking_ref(self):
        # create ref using uuid
        return uuid.uuid4().hex.upper()

    # set status to paid and confirmed
    def status_to_paid_and_confirmed(self):
        self.status = self.StatusChoices.PAIDANDCONFIRMED
        self.save()

    def save(self, *args, **kwargs):
        # if not set, create booking ref
        if not self.booking_id:
            self.booking_id = self.create_booking_ref()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.booked_vehicle.nickname}"
