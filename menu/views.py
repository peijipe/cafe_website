from django.shortcuts import render
from menu.models import Menu
from menu.models import Course


def index(request):
    menus = Menu.objects.all()
    courses = Course.objects.all()
    context = {
                'menus': menus,
                'courses': courses
               }

    return render(request, 'menu/index.html', context)


def detail(request):
    courses = Course.objects.all()
    return render(request, 'menu/detail.html', {'courses': courses})
