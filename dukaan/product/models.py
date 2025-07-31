from django.db import models

# Create your models here.
class Item(models.Model):
    p_name= models.CharField(max_length=100)
    p_quantity = models.IntegerField()
    p_price = models.IntegerField()
    p_discount = models.IntegerField()