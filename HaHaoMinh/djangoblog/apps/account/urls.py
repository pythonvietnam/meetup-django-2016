from django.conf.urls import url
from django.contrib import admin

from .views import (
    register,
    register_success,
    user_login,
)

urlpatterns = [
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^login/$', user_login),
    # url(r'^login/success/$', logged_in),
    # url(r'^signup/$', sign_up),
]
