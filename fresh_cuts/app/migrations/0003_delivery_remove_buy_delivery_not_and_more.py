# Generated by Django 5.0.1 on 2024-09-17 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_buy_payment_status_product_quantity_shopreg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rout', models.TextField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('password', models.IntegerField()),
                ('name', models.TextField()),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='buy',
            name='delivery_not',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='productid',
        ),
        migrations.AddField(
            model_name='buy',
            name='del_boy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='buy',
            name='product',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buy',
            name='date_of_buying',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='buy',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='buy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register'),
        ),
        migrations.CreateModel(
            name='delpro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('date', models.TextField(null=True)),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.buy')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.delivery')),
            ],
        ),
    ]