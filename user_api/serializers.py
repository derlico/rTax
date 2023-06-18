from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'barcode', 'cost', 'price', 'tax']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'group', 'location']

class SaleSerializer(serializers.ModelSerializer):
     class Meta:
         model = Sale
         fields = ['id', 'sale_total']
         