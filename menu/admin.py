from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_position', 'is_featured')
    list_filter = ('is_featured', 'image_position')
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_special')
    list_filter = ('category', 'is_special')
    search_fields = ('name', 'description')
    ordering = ('category', 'name')