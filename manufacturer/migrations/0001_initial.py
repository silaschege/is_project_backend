# Generated by Django 4.0.3 on 2022-11-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManufactureRegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufactureName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
