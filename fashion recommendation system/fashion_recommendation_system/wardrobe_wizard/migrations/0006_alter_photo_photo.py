# Generated by Django 5.0.6 on 2024-06-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe_wizard', '0005_alter_photo_photo_delete_lower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='cloths/'),
        ),
    ]
