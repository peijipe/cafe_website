from django.urls import path
from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('contact/confirm', views.contact, name='confirm'),
    path('contact/thanks', views.thanks, name='thanks'),
]