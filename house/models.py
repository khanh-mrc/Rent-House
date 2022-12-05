from django.db import models
from datetime import datetime
from accounts.models import Profile

# Create your models here.pyth
class Listing(models.Model):
    status_choices = (
        ("Available","Available"),
        ("Unvailable", "Unavailable"),
        ("Sale", "For Sale"),
    )
    city_choices = {
        ('TP. Hồ Chí Minh', 'TP. Hồ Chí Minh'),
        ('Hà Nội', 'Hà Nội'),
        ('Đà Nẵng', 'Đà Nẵng'),
    }
    status = models.CharField(max_length = 20, choices=status_choices, default="Available")
    lessor = models.ForeignKey(Profile,on_delete = models.CASCADE, blank=True,null=True)
    title = models.CharField(max_length = 120)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100,choices=city_choices,default='TP. Hồ Chí Minh')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    area = models.IntegerField()
    floor= models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=0)
    kitcheen = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.BooleanField(default=0)
    AirCondition = models.BooleanField(default=0)
    ComunityCenter = models.BooleanField(default=0)
    SecuritySystem = models.BooleanField(default=0)
    Furniture = models.TextField(default=0)
    list_date = models.DateField(default = datetime.now,blank = True)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank =True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank =True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank =True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank =True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank =True)
    def __str__(self):
        return  self.title

