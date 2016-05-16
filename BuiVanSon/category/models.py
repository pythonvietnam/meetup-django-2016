from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(blank=False, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
