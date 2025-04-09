from django.contrib import admin
from .models import Category, MenuItem
from cloudinary.forms import CloudinaryFileField
from django.core.files.storage import default_storage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_position', 'is_featured')
    list_filter = ('is_featured', 'image_position')
    search_fields = ('name',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            return CloudinaryFileField(
                options={
                    'folder': 'category_images',
                    'tags': ['admin_upload'],
                    'resource_type': 'image'
                }
            )
        return super().formfield_for_dbfield(db_field, **kwargs)

    def save_model(self, request, obj, form, change):
        print("Current storage backend for media:", default_storage.__class__)
        super().save_model(request, obj, form, change)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_special')
    list_filter = ('category', 'is_special')
    search_fields = ('name', 'description')
    ordering = ('category', 'name')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            return CloudinaryFileField(
                options={
                    'folder': 'menu_items',
                    'tags': ['admin_upload'],
                    'resource_type': 'image'
                }
            )
        return super().formfield_for_dbfield(db_field, **kwargs)