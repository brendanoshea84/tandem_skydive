# Generated by Django 3.0.7 on 2020-08-14 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_cost',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='quantity',
        ),
    ]
