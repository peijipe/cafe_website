from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


def index(request):

    keywords = request.GET.get("keyword")

    if keywords:
        keyword_list = keywords.replace('　', ' ').split(' ')

        search_posts = Post.objects.all()

        for keyword in keyword_list:
            search_posts = search_posts.filter(title__contains=keyword)

        search_posts = search_posts.order_by('-created_datetime')
        return render(request, 'news/index.html', {'posts': search_posts, 'keywords': keywords})

    posts = Post.objects.all().order_by('-created_datetime')
    return render(request, 'news/index.html', {'posts': posts})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/detail.html', {"post": post})

