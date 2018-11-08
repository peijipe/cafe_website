from django.shortcuts import render, redirect
from news.models import Post
from menu.models import Menu
from mainpage.models import Contact

from .forms import ContactForm


def index(request):
    posts = Post.objects.all().order_by('-created_datetime')[:3]
    menus = Menu.objects.all()

    context = {
               'posts': posts,
               'menus': menus,
               }

    return render(request, 'mainpage/index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        obj = Contact.objects.create(name=name, email=email, message=message)
        print(obj)
        return render(request, 'mainpage/confirm.html', {'obj': obj})

    return render(request, 'mainpage/contact.html', {'form': form})


def confirm(request):
    return render(request, 'mainpage/confirm.html', )


def thanks(request):
    return HttpResponseRedirect('/thanks/')