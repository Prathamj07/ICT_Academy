from django.urls import path

from product.views import item_view
from customer.views import customer_details


urlpatterns = [
    path('', customer_details, name='customer'),# Home page route
    
]