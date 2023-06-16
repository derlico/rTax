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


class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=60, unique=True)
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
    group = models.CharField(
          max_length=20,
          choices=CUSTOMER_GROUP_OPTIONS,
          default = 0,
    )
    location = models.CharField(max_length=100)
    #date_added = models.DateTimeField(datetime.datetime.now())
    
    def __str__(self):
        return self.name + ": "+ self.phone