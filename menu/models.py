from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)  # Stored in Neon
    is_featured = models.BooleanField(default=False)  # Stored in Neon
    image = CloudinaryField(
        'image', 
        folder='category_images',
        default='default_category',  # Set a default image public_id
       
    ) # Stored in Cloudinary
    image_position = models.CharField(  # Stored in Neon
        max_length=5,
        choices=[('left', 'Left'), ('right', 'Right')],
        default='left'
    )
class MenuItem(models.Model):
    name = models.CharField(max_length=100)  # Stored in Neon
    description = models.TextField(blank=True)  # Stored in Neon
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Stored in Neon
    #image = CloudinaryField('image', folder='menu_items')  # Stored in Cloudinary
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items'     )  # Stored in Neon
    is_special = models.BooleanField(default=False)  # Stored in Neon
    
    def __str__(self):
        return self.name