from __future__ import unicode_literals

from django.db import models


class ContactModel(models.Model):
    email = models.EmailField(blank=False, max_length=255)
    subject = models.CharField(blank=False, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    message = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
