from __future__ import unicode_literals

from django.db import models
class category (models.Model):
	name = models.CharField(blank=False, max_length=255)
	slug = models.SlugField(blank=False, max_length=255)
	def __str__(self):
		return self.name
# Create your models here.
