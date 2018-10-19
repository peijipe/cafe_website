from django.shortcuts import render
from news.models import Post
from menu.models import Menu


def index(request):
    posts = Post.objects.all().order_by('-created_datetime')[:3]

    pizzas = Menu.objects.filter(category=1)
    pastas = Menu.objects.filter(category=2)
    salads = Menu.objects.filter(category=3)

    context = {
               'posts': posts,
               'pizzas': pizzas,
               'pastas': pastas,
               'salads': salads
               }

    return render(request, 'mainpage/index.html', context)
