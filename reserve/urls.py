from django.urls import path
from . import views

app_name = 'reserve'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reserve_id>', views.detail, name='detail'),
    path('new_reserve', views.reserve_new, name='new_reserve'),
    path('<int:reserve_id>/edit', views.edit, name='edit'),
    # path('<int:reserve_id>/delete/', views.delete, name='delete'),

]
