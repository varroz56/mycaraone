from datetime import date
from django.db import models


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

    closed_on = models.DateTimeField(auto_now_add=False, blank=True, null=True)
