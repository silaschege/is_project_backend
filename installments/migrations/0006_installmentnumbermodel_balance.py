# Generated by Django 4.0.3 on 2022-11-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installments', '0005_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='installmentnumbermodel',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
