# Generated by Django 4.0.5 on 2022-06-18 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='User_image'),
        ),
    ]
