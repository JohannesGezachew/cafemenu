from django.db import migrations
from cloudinary import uploader

def forward_migration(apps, schema_editor):
    Category = apps.get_model('menu', 'Category')
    for category in Category.objects.all():
        if not category.image:  # Skip if no image
            continue
            
        # Check if already a Cloudinary resource
        if hasattr(category.image, 'url'):  # Already Cloudinary
            continue
            
        try:
            # Handle case where image might be a path or file
            if hasattr(category.image, 'path'):
                result = uploader.upload(category.image.path)
            else:
                # Fallback for string paths
                result = uploader.upload(str(category.image))
                
            category.image = result['public_id']
            category.save()
        except Exception as e:
            print(f"Failed to migrate image for category {category.id}: {e}")

def reverse_migration(apps, schema_editor):
    pass  # No reversal needed

class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0018_remove_menuitem_weight_alter_category_image_and_more'),
    ]
    
    operations = [
        migrations.RunPython(forward_migration, reverse_migration),
    ]