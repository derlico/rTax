# Generated by Django 4.2.2 on 2023-06-18 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_api.customer'),
        ),
    ]
