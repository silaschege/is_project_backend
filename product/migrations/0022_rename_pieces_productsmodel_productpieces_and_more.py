# Generated by Django 4.0.3 on 2022-10-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_productsmodel_pieces_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsmodel',
            old_name='Pieces',
            new_name='productPieces',
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='productPrice',
            field=models.IntegerField(),
        ),
    ]
