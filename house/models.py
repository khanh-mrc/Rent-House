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
        ('Bình Dương','Bình Dương'),
        ('An Giang','An Giang'),
        ('Bà Rịa – Vũng Tàu','Bà Rịa – Vũng Tàu'),
        ('Bạc Liêu','Bạc Liêu'),
        ('Bắc Giang','Bắc Giang'),
        ('Bắc Kạn','Bắc Kạn'),
        ('Bắc Ninh','Bắc Ninh'),
        ('Bến Tre','Bến Tre'),
        ('Bình Định','Bình Định'),
        ('Bình Phước','Bình Phước'),
        ('Bình Thuận','Bình Thuận'),
        ('Cà Mau','Cà Mau'),
        ('Cao Bằng','Cao Bằng'),
        ('Cần Thơ','Cần Thơ'),
        ('Đắk Lắk','Đắk Lắk'),
        ('Đắk Nông','Đắk Nông'),
        ('Điện Biên','Điện Biên'),
        ('Đồng Nai','Đồng Nai'),
        ('Đồng Tháp','Đồng Tháp'),
        ('Gia Lai','Gia Lai'),
        ('Hà Giang','Hà Giang'),
        ('Hà Nam','Hà Nam'),
        ('Hà Tĩnh','Hà Tĩnh'),
        ('Hải Dương','Hải Dương'),
        ('Hải Phòng','Hải Phòng'),
        ('Hậu Giang','Hậu Giang'),
        ('Hòa Bình','Hòa Bình'),
        ('Hưng Yên','Hưng Yên'),
        ('Khánh Hòa','Khánh Hòa'),
        ('Kiên Giang','Kiên Giang'),
        ('Kon Tum','Kon Tum'),
        ('Lai Châu','Lai Châu'),
        ('Lạng Sơn','Lạng Sơn'),
        ('Lào Cai','Lào Cai'),
        ('Lâm Đồng','Lâm Đồng'),
        ('Long An','Long An'),
        ('Nam Định','Nam Định'),
        ('Nghệ An','Nghệ An'),
        ('Ninh Bình','Ninh Bình'),
        ('Ninh Thuận','Ninh Thuận'),
        ('Phú Thọ','Phú Thọ'),
        ('Phú Yên','Phú Yên'),
        ('Quảng Bình','Quảng Bình'),
        ('Quảng Nam','Quảng Nam'),
        ('Quảng Ngãi','Quảng Ngãi'),
        ('Quảng Ninh','Quảng Ninh'),
        ('Quảng Trị','Quảng Trị'),
        ('Sóc Trăng','Sóc Trăng'),
        ('Sơn La','Sơn La'),
        ('Tây Ninh','Tây Ninh'),
        ('Thái Bình','Thái Bình'),
        ('Thái Nguyên','Thái Nguyên'),
        ('Thanh Hóa','Thanh Hóa'),
        ('Thừa Thiên Huế','Thừa Thiên Huế'),
        ('Tiền Giang','Tiền Giang'),
        ('Trà Vinh','Trà Vinh'),
        ('Tuyên Quang','Tuyên Quang'),
        ('Vĩnh Long','Vĩnh Long'),
        ('Vĩnh Phúc','Vĩnh Phúc'),
        ('Yên Bái','Yên Bái'),
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

