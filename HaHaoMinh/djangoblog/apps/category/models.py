from __future__ import unicode_literals

from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(blank=False, max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
