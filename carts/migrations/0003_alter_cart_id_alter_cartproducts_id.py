# Generated by Django 4.2.7 on 2023-11-12 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
