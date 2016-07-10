from django.conf.urls import url

from .views import CareerViews

urlpatterns = [
    url(r'^$', CareerViews.submitform, name='form'),
    url(r'^sent/$', CareerViews.submitform_sent, name='form_sent'),
]
