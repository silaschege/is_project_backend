# Generated by Django 4.0.3 on 2022-10-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_productsmodel_packagingquantity'),
        ('installments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installmentmodel',
            name='product_id',
            field=models.ManyToManyField(to='product.productsmodel'),
        ),
    ]
