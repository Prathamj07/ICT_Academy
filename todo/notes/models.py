from django.db import models
import datetime

# Create your models here.


class test(models.Model):
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=100)
    task = models.CharField(max_length=200)
    

    
    