# Generated by Django 4.0.3 on 2022-10-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_categoryname_productnamemodel_productname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='packagingQuantity',
            field=models.CharField(choices=[('kg', 'Kilogram'), ('mg', 'Milligrams'), ('ltr', 'Liter'), ('ml', 'Milliliter')], default='kg', max_length=3),
        ),
    ]
