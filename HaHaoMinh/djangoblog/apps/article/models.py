from __future__ import unicode_literals

from ..category.models import CategoryModel
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


def upload_location(instance, filename):
    # Custom filename
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" % (instance.id, instance.id, extension)
    return "%s/%s" % (instance.id, filename)


class ArticleModel(models.Model):
    name = models.CharField(blank=False, max_length=255)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_location,
        blank=True, null=True,
        width_field="width_field", height_field="height_field",
    )
    slug = models.SlugField(unique=False)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        # import pdb
        # pdb.set_trace()
        # Return slug format /articles/id/
        # return reverse("articles:article_detail", kwargs={"slug": self.slug})
        return "/articles/%s/" % self.slug

    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = ArticleModel.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_article_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_article_receiver, sender=ArticleModel)
