# Generated by Django 4.1.2 on 2022-10-27 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_order_date_delivery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categorie'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product'},
        ),
    ]
