# Generated by Django 4.0.3 on 2023-03-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudAPP', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default/user.png', null=True, upload_to='images/'),
        ),
    ]