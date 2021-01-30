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
