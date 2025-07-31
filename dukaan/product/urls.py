from django.urls import path

from product.views import item_view ##This is optimized
from customer.views import customer_details
from bill.views import create_bill


urlpatterns = [
    path('', item_view, name='product'),# Home page route
    path('/customer', customer_details, name='customer'),    
    path('/bill', create_bill, name='bill'),    
]