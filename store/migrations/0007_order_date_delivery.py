# Generated by Django 4.1.2 on 2022-10-27 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_delivery',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]