# Generated by Django 4.1.2 on 2022-10-30 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_order_totalprice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='TotalPrice',
        ),
    ]
