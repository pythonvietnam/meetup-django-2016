from __future__ import unicode_literals

from ..category.models import CategoryModel
from django.db import models
from django.core.urlresolvers import reverse


class ArticleModel(models.Model):
    name = models.CharField(blank=False, max_length=255)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        # Return slug format /articles/id/
        return reverse("articles:article_detail", kwargs={"id": self.id})
        # return "/posts/%s/" % self.id
