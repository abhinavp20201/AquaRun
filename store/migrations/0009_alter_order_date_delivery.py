# Generated by Django 4.1.2 on 2022-10-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_date_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateField(blank=b'I01\n', default=''),
        ),
    ]
