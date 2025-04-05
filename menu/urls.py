from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/menu/', views.menu_list, name='menu_list'),
    path('', views.menu_list, name='menu_list'),
]
