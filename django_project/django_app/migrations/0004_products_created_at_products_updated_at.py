# Generated by Django 5.0.2 on 2024-03-09 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_remove_products_compney_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 9, 11, 22, 32, 817721)),
        ),
        migrations.AddField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 9, 11, 22, 32, 817721)),
        ),
    ]
