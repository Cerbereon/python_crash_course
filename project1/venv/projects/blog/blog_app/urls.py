'''Defines URL patterns for blogg_app.'''

from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
]