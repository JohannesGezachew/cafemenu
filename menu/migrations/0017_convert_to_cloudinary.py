from django.db import migrations
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0014_alter_menuitem_category'),  # Replace with actual previous migration
    ]
    
    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.AlterField(
                    model_name='category',
                    name='image',
                    field=django.db.models.fields.CharField(max_length=255),
                ),
            ]
        )
    ]