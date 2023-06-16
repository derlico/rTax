from typing import Any
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
""" class AppUserManager(BaseUserManager):
    def create_user() """
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name