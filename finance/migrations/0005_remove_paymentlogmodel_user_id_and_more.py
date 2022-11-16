# Generated by Django 4.0.3 on 2022-11-16 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0004_remove_paymentlogmodel_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlogmodel',
            name='user_id',
        ),
        migrations.AddField(
            model_name='paymentlogmodel',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
