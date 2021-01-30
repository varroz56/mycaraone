from django.db import models


# Manufacturer model stores basic information about the manufacturer
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
