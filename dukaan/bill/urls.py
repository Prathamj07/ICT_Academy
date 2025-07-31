from django.urls import path

from bill.views import create_bill, total_bill


urlpatterns = [
    path('', create_bill, name='bill'),
    path('<int:bill_id>', total_bill, name='show_bill')
    
]