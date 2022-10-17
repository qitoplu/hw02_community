from django.shortcuts import render, get_object_or_404
from .models import Post, Group
POSTS_QUANTITY = 10


def index(request):
    posts = Post.objects.select_related('group')[:POSTS_QUANTITY]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all()[:POSTS_QUANTITY]
    context = {
        'groups': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
