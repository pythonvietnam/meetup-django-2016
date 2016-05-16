from django.conf.urls import url
from django.contrib import admin

from .views import (
    contact_form,
    contact_form_sent
)

urlpatterns = [
    url(r'^$', contact_form),
    url(r'^sent/$', contact_form_sent),
]
