from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^atik/$', views.atik_blog, name='atik'),
    url(r'^(?P<slug>[\w\-]+)/$', views.atik),
]