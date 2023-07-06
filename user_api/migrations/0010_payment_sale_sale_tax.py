# Generated by Django 4.2.2 on 2023-06-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0009_rename_product_sale_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Mpesa', 'Mpesa'), ('Bank', 'Bank'), ('Other', 'Other')], default='Cash', max_length=50)),
                ('payment_total', models.CharField(max_length=60)),
                ('payment_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='sale_tax',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
    ]