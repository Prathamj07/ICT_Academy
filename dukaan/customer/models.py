from django.db import models

# Create your models here.
class customer(models.Model):
    c_name= models.CharField(max_length=100)
    c_contact = models.IntegerField()
    c_address = models.CharField(max_length=100)