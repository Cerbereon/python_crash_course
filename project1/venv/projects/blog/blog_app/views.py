from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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


@login_required
def new_post(request):
    '''A page for adding post.'''
    if request.method != 'POST':
        # No data submitting; create a blank form
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blog_app:posts'))

    context = {'form': form}
    return render(request, 'blog_app/new_post.html', context)


@login_required
def edit_post(request, post_id):
    '''A page for editing a post.'''
    post = Post.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill with the current entry
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_app:posts'))

    context = {'post': post, 'form': form}
    return render(request, 'blog_app/edit_post.html', context)
