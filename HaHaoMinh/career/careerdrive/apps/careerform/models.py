from __future__ import unicode_literals

from django.db import models


class Career(models.Model):
  fullname = models.CharField(blank=False, max_length=128)
  birthday = models.DateField(blank=False)
  gender = models.CharField(blank=False, max_length=10)
  email = models.EmailField(blank=False, max_length=128)
  phone = models.CharField(blank=False, max_length=13)
  address = models.CharField(blank=False, max_length=255)
  attachment = models.FileField(null=True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

  def __unicode__(self):
    return self.fullname

  def __str__(self):
    return self.fullname


  class Meta:
    db_table = "profile"