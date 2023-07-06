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
    ('0', 'ZERO-RATED'),
    ('0', 'EXEMPTED'),
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

class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=60, null=True)
    cost = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    tax = models.CharField(
          max_length=20,
          choices=TAX_OPTIONS,
          default = 0,
    )
    #date_added = models.DateTimeField(datetime.datetime.now())
    
    def __str__(self):
        return self.name

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
        return self.name + ": " + self.phone

class Sale(models.Model):
    products = models.ManyToManyField(Product)
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True)
    sale_total = models.CharField(max_length=60)
    sale_tax = models.CharField(max_length=60)
    #date_added = models.DateTimeField(datetime.datetime.now())
    
    def __str__(self):
        return "Sale Value- Ksh "+ self.sale_total

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