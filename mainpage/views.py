from django.shortcuts import render
from news.models import Post


def index(request):
    posts = Post.objects.all().order_by('-created_datetime')[:3]
    return render(request, 'mainpage/index.html', {'posts': posts})

