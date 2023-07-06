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
         fields = ['id', 'customer', 'sale_total', 'products']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_type', 'payment_total', 'payment_name']
         