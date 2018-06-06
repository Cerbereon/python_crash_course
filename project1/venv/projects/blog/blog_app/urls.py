'''Defines URL patterns for blogg_app.'''

from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all posts.
    url(r'^posts/$', views.posts, name='posts'),

    # Page for adding post
    url(r'^new_post/$', views.new_post, name='new_post'),

    # Page for editing post
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post,
        name='edit_post'),
]