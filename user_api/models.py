import datetime
from typing import Any
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
""" class AppUserManager(BaseUserManager):
    def create_user() """
    
TAX_OPTIONS = (
    ('16', 'VAT(16%)'),
    ('0', 'NO TAX'),
)

CUSTOMER_GROUP_OPTIONS = (
    ('0', 'Physical Customers'),
    ('1', 'Online Customers'),
    ('2', 'Hybrid Customers'),
)

PAYMENT_METHODS = (
    ('0', 'Cash'),
    ('1', 'Mpesa'),
    ('2', 'Bank'),
    ('3', 'Other')
)

# PRODUCT MODEL 
class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=60, null=True)
    cost = models.FloatField(max_length=50)
    price = models.FloatField(max_length=50)
    tax = models.CharField(
          max_length=20,
          choices=TAX_OPTIONS,
          default = 0,
    )
    #date_added = models.DateTimeField(datetime.datetime.now())
    
    def __str__(self):
        return self.name


# STOCK MODEL
class Stock(models.Model):
    stockID =  models.AutoField(primary_key=True)
    productID = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.BigIntegerField()
    #date_added = models.DateTimeField(datetime.datetime.now())
    
    def __str__(self):
        return "Product: " + str(self.productID) + " Qty: " + str(self.quantity)

# CUSTOMER MODEL
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=60)
    email = models.CharField(max_length=200, null=True)
    group = models.CharField(
          max_length=20,
          choices=CUSTOMER_GROUP_OPTIONS,
          default = 0,
    )
    location = models.CharField(max_length=100)
    #date_added = models.DateTimeField(datetime.datetime.now())
    
    def __str__(self):
        return self.name

# SALES MODEL
class Sale(models.Model):
    sale_ref = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    sale_total = models.FloatField()
    sale_tax = models.FloatField()
    #date_added = models.DateTimeField(datetime.datetime.now())
    
    def __str__(self):
        return "Sale Ref "+ str(self.sale_ref)

# SALE_PRODUCT MODEL

class SaleProduct(models.Model):
    sale_ref = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return "Sale Product Ref "+ str(self.sale_ref) + str(self.product)



class Payment(models.Model):
    payment_type = models.CharField(
          max_length=50,
          choices=PAYMENT_METHODS,
          default = 'Cash',
    )
    payment_total = models.CharField(max_length=60)
    payment_name = models.CharField(max_length=200)

    def __str__(self):
        return self.payment_name + "- Ksh "+ self.payment_total