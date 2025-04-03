from django.urls import path
from . import views

urlpatterns = [
    path('admin/menu/', views.menu_list, name='menu_list'),
    path('', views.menu_list, name='menu_list'),
]