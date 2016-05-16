from django.conf.urls import url
from django.contrib import admin

from .views import (
    article_list,
    article_create,
    article_detail,
    article_update,
    article_delete
)

urlpatterns = [
    url(r'^$', article_list, name="article_list"),
    url(r'^create/$', article_create, name="article_create"),
    url(r'(?P<id>\d+)/$', article_detail, name="article_detail"),
    url(r'(?P<id>\d+)/edit/$', article_update, name="article_update"),
    url(r'(?P<id>\d+)/delete/$', article_delete, name="article_delete"),
]
