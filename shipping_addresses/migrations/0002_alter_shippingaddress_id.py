# Generated by Django 4.2.7 on 2023-11-12 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
