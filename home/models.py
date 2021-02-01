from django.db import models
# import settings to use env vars
from django.conf import settings
# import django builtin send email method
from django.core.mail import send_mail
# import our models
# Contact message model


class ContactUsMessage(models.Model):
    """ A model to store messages from the contact form"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email
