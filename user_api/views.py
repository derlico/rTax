from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#PRODUCT VIEWS
@api_view(['GET', 'POST']) #decorater
def product_list(request):
    
    if request.method == 'GET':
        #get all products
        products = Product.objects.all()
        #serailize the products
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #return json list
        #return JsonResponse(serializer.data, safe=False)
        #return json dictionary
        #return JsonResponse({"products": serializer.data})
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    
    #searching if valid product
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #defining endpoint menthods based on request type
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#STOCK VIEWS
@api_view(['GET', 'POST'])
def stocks_list(request):
    
    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#CUSTOMER VIEWS
@api_view(['GET', 'POST'])
def customer_list(request):
    
    if request.method == 'GET':
        #get all products
        customers = Customer.objects.all()
        #serailize the products
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
        #return json list
        #return JsonResponse(serializer.data, safe=False)
        #return json dictionary
        #return JsonResponse({"products": serializer.data})
    
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, id):
    
    #searching if valid product
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #defining endpoint menthods based on request type
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#SALES VIEWS
@api_view(['GET', 'POST'])
def sales_list(request):
    
    if request.method == 'GET':
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def sale_detail(request, id):
    
    #searching if valid product
    try:
        sale = Sale.objects.get(pk=id)
    except Sale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #defining endpoint menthods based on request type
    if request.method == 'GET':
        serializer = SaleSerializer(sale)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def payments_list(request):
    if request.method == 'GET':
        sales = Payment.objects.all()
        serializer = PaymentSerializer(sales, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
