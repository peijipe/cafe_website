from django.shortcuts import render
from menu.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'reserve/index.html', {'courses': courses})

