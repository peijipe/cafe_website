from django.shortcuts import render
from menu.models import Menu


def index(request):
    menus = Menu.objects.all()
    pizzas = Menu.objects.filter(category=1)
    pastas = Menu.objects.filter(category=2)
    salads = Menu.objects.filter(category=3)

    context = {'menus': menus,
               'pizzas': pizzas,
               'pastas': pastas,
               'salads': salads
               }

    return render(request, 'menu/index.html', context)
