from __future__ import unicode_literals

from django.db import models


# Create your models here.

# Create form class for the Registration form
class RegistrationModel(models.Model):
    username = models.CharField(blank=False, max_length=120)
    email = models.EmailField(blank=False, max_length=120)
    password = models.CharField(blank=False, max_length=120)  # Set the widget to # PasswordInput
    password2 = models.CharField(blank=False, max_length=120)  # Set the widget to
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
