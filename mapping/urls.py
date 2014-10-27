from django.conf.urls import patterns, url
__author__ = 'songqiaosu'

from mapping import views

urlpatterns = patterns('',
    url(r'^(?P<keyword>[a-zA-Z]*)$', views.index, name='index'),
)


