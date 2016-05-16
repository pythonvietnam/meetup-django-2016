from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name  =  models.CharField(blank=False,   max_length=255)
    title      =  models.CharField(blank=False,   max_length=255)
    email      =  models.EmailField(blank=False,  max_length=255)
    content    =  models.TextField()
