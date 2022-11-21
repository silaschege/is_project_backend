# Generated by Django 4.0.3 on 2022-11-07 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('installments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shipping_status', models.CharField(choices=[('SH', 'SHIPPING'), ('IT', 'INTRANSIT'), ('REC', 'RECEIVED')], default='SH', max_length=5)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('installment', models.ManyToManyField(to='installments.installmentnumbermodel')),
            ],
        ),
    ]
