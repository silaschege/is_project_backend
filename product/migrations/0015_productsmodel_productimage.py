# Generated by Django 4.0.3 on 2022-10-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_productsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='productImage',
            field=models.ImageField(default='media/product_images/Screenshot_2022-09-12_at_16.00.36.png', upload_to='product_images/'),
        ),
    ]
