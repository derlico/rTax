# Generated by Django 4.2.2 on 2023-06-18 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0006_remove_sale_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_api.customer'),
        ),
    ]
