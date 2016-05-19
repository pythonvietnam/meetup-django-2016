from __future__ import unicode_literals

from ..category.models import CategoryModel
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.conf import settings
import datetime


def upload_location(instance, filename):
    today = datetime.date.today().strftime("%Y/%B/%d")
    # Custom filename
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" % (instance.id, instance.id, extension)
    return "%s/%s" % (today, filename)


class ArticleModel(models.Model):
    name = models.CharField(blank=False, max_length=255)
    image = models.ImageField(
        upload_to=upload_location,
        blank=True, null=True,
        width_field="width_field", height_field="height_field",
    )

    slug = models.SlugField(unique=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryModel)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        # Return slug format /articles/id/
        # return reverse("articles:article_detail", kwargs={"slug": self.slug})
        return "/articles/%s-%s/" % (self.slug, self.id)

    class Meta:
        ordering = ["-timestamp", "-updated"]


def pre_save_article_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = ''.join(map(lambda x: slugify(x), [instance]))


pre_save.connect(pre_save_article_receiver, sender=ArticleModel)
