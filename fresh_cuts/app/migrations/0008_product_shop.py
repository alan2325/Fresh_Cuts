# Generated by Django 5.0.1 on 2024-09-26 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_shopreg_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.shopreg'),
            preserve_default=False,
        ),
    ]
