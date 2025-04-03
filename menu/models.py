from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    image_position = models.CharField(
        max_length=5,
        choices=[('left', 'Left'), ('right', 'Right')],
        default='left'
    )

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items'  # This is what you'll use to access items
    )
    is_special = models.BooleanField(default=False)
    weight = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name