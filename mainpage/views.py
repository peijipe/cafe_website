from django.shortcuts import render
from news.models import Post
from menu.models import Menu


def index(request):
    posts = Post.objects.all().order_by('-created_datetime')[:3]
    menus = Menu.objects.all()

    context = {
               'posts': posts,
               'menus': menus,
               }

    return render(request, 'mainpage/index.html', context)
