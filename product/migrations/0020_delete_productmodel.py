# Generated by Django 4.0.3 on 2022-10-24 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installments', '0002_alter_installmentmodel_product_id'),
        ('product', '0019_productsmodel_packagingquantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductModel',
        ),
    ]
