from django.db import migrations
from cloudinary.uploader import upload

def forward_migration(apps, schema_editor):
    Category = apps.get_model('menu', 'Category')
    for category in Category.objects.exclude(image=''):
        if not category.image.startswith(('http', 'cloudinary:')):
            try:
                # Upload to Cloudinary if it's a local file path
                result = upload(category.image.path)
                category.image = result['public_id']
                category.save()
            except Exception as e:
                print(f"Failed to migrate image for category {category.id}: {e}")
                category.image = 'default_category'
                category.save()

def reverse_migration(apps, schema_editor):
    pass  # Cannot reverse this operation

class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0018_remove_menuitem_weight_alter_category_image_and_more'),  # Your previous migration
    ]
    
    operations = [
        migrations.RunPython(forward_migration, reverse_migration),
    ]