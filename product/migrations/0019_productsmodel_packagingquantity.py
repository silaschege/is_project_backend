# Generated by Django 4.0.3 on 2022-10-24 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_packagingquantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='packagingQuantity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.packagingquantity'),
        ),
    ]
