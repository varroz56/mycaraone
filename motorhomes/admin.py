from django.contrib import admin

from .models import Manufacturer, Vehicle, Motorhome

admin.site.register(Manufacturer)
admin.site.register(Vehicle)
admin.site.register(Motorhome)
