# Generated by Django 4.0.3 on 2022-11-15 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlogmodel',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='paymentlogmodel',
            name='paymentMethod',
        ),
        migrations.RemoveField(
            model_name='paymentlogmodel',
            name='totalAmountPaid',
        ),
    ]
