from django.urls import path
from user_api import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>', views.product_detail),
    path('customers/', views.customer_list),
    path('customers/<int:id>', views.customer_detail),
    path('sales/', views.sales_list),
    path('sales/<int:id>', views.sale_detail),
    
]