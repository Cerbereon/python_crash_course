'''Defines URL patterns for learning_logs.'''

from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.index, name='index')
]