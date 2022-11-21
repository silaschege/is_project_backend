# Generated by Django 4.0.3 on 2022-11-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(max_length=7)),
                ('totalAmountPaid', models.FloatField(max_length=7)),
                ('balance', models.FloatField(max_length=7)),
                ('timePaid', models.DateTimeField(auto_now_add=True)),
                ('paymentMethod', models.CharField(max_length=255)),
            ],
        ),
    ]
