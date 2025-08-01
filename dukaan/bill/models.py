from django.db import models
from customer.models import customer
from product.models import Item
import datetime
# Create your models here.


class bill(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    total_amount = models.FloatField(default = 0.0)
    
class billItem(models.Model):
    bill = models.ForeignKey(bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

