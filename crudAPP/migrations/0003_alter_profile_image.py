# Generated by Django 4.0.3 on 2023-03-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudAPP', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
