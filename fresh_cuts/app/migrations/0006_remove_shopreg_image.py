# Generated by Django 5.0.1 on 2024-09-24 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_shopreg_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopreg',
            name='image',
        ),
    ]
