# Generated by Django 4.0.3 on 2022-10-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_delete_productmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='Pieces',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='productPrice',
            field=models.IntegerField(default=1),
        ),
    ]
