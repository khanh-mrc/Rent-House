from django.db import models
from datetime import datetime
# Create your models here.
class House(models.Model):
    title = models.CharField(max_length = 120)
    address = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    area = models.IntegerField()
    bedrooms = models.IntegerField()
    badrooms = models.IntegerField()
    floors = models.IntegerField()
    furniture = models.TextField(blank=True)
    list_date = models.DateField(default = datetime.now,blank = True)
    def __str__(self):
        return  self.title


