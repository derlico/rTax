# Generated by Django 4.2.2 on 2023-06-16 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0006_alter_product_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
    ]