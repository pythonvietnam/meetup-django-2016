from django.conf.urls import url
from django.contrib import admin

from .views import (
    sign_in,
    sign_up
)

urlpatterns = [
    url(r'^signin/$', sign_in),
    url(r'^signup/$', sign_up),
]
