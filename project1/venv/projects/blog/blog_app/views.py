from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    '''The home page for blog.'''
    return render(request, 'blog_app/index.html')


def posts(request):
    '''Show all posts.'''
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blog_app/posts.html', context)


def new_post(request):
    '''A page for adding post.'''
    if request.method != 'POST':
        # No data submitting; create a blank form
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_app:posts'))

    context = {'form': form}
    return render(request, 'blog_app/new_post.html', context)
