# Generated by Django 4.1.2 on 2022-10-27 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_cash_customer_remove_cash_price_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cash',
        ),
    ]
