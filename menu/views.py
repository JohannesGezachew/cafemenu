from django.shortcuts import render
from .models import Category

def menu_list(request):
    categories = Category.objects.prefetch_related('menu_items').all()
    return render(request, 'menu/menu_list.html', {'categories': categories})