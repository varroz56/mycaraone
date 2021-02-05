from django.contrib import admin

from .models import BillingAddress, BookingSummary
# Register your models here.

admin.site.register(BillingAddress)
admin.site.register(BookingSummary)