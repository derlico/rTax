# Generated by Django 4.2.2 on 2023-06-16 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_customer_product_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
    ]
