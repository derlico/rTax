# Generated by Django 4.2.2 on 2023-06-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0010_payment_sale_sale_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('0', 'Cash'), ('1', 'Mpesa'), ('2', 'Bank'), ('3', 'Other')], default='Cash', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(max_length=60, null=True),
        ),
    ]