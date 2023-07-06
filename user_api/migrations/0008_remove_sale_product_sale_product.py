# Generated by Django 4.2.2 on 2023-06-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0007_sale_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ManyToManyField(to='user_api.product'),
        ),
    ]
