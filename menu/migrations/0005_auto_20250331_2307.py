# Generated by Django 3.2.6 on 2025-03-31 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20250331_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['category', 'name']},
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='image_position',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload image for this category', null=True, upload_to='category_images/'),
        ),
        migrations.AddField(
            model_name='category',
            name='image_position',
            field=models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default='left', help_text='Image display position', max_length=5),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menu.category'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(help_text='Price in whole numbers (e.g., 460 for $4.60)'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='weight',
            field=models.CharField(blank=True, help_text="Item weight (e.g., '160 GM')", max_length=20),
        ),
    ]
