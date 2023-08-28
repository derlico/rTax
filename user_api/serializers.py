from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'barcode', 'cost', 'price', 'tax']

class StockSerializer(serializers.ModelSerializer):
     class Meta:
         model = Stock
         fields = ['stockID', 'productID', 'quantity']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'group', 'location']

class SaleSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    product_name = serializers.StringRelatedField()
    class Meta:
         model = Sale
         fields = '__all__'
    
    def get_product_name(self, obj):
        return obj.product.name
   
""" class SaleSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    class Meta:
         model = Sale
         fields = ('id', 'customer', 'customer_name', 'sale_total', 'products', 'sale_tax')
    def get_customer_name(self, obj):
        return obj.customer.name """

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_type', 'payment_total', 'payment_name']
         