# Generated by Django 4.1.3 on 2022-12-29 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0033_alter_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Lạng Sơn', 'Lạng Sơn'), ('Thái Bình', 'Thái Bình'), ('Kon Tum', 'Kon Tum'), ('Cà Mau', 'Cà Mau'), ('Hải Dương', 'Hải Dương'), ('Hà Tĩnh', 'Hà Tĩnh'), ('Nam Định', 'Nam Định'), ('Điện Biên', 'Điện Biên'), ('Cần Thơ', 'Cần Thơ'), ('Lâm Đồng', 'Lâm Đồng'), ('Hà Nội', 'Hà Nội'), ('Quảng Ninh', 'Quảng Ninh'), ('Kiên Giang', 'Kiên Giang'), ('Đà Nẵng', 'Đà Nẵng'), ('Tuyên Quang', 'Tuyên Quang'), ('Ninh Thuận', 'Ninh Thuận'), ('Bến Tre', 'Bến Tre'), ('Ninh Bình', 'Ninh Bình'), ('Trà Vinh', 'Trà Vinh'), ('Bắc Ninh', 'Bắc Ninh'), ('Bình Thuận', 'Bình Thuận'), ('TP. Hồ Chí Minh', 'TP. Hồ Chí Minh'), ('Vĩnh Phúc', 'Vĩnh Phúc'), ('Bình Dương', 'Bình Dương'), ('Quảng Trị', 'Quảng Trị'), ('Bình Phước', 'Bình Phước'), ('Phú Yên', 'Phú Yên'), ('Hà Nam', 'Hà Nam'), ('Đồng Tháp', 'Đồng Tháp'), ('Thái Nguyên', 'Thái Nguyên'), ('Thừa Thiên Huế', 'Thừa Thiên Huế'), ('Nghệ An', 'Nghệ An'), ('Bình Định', 'Bình Định'), ('Bắc Giang', 'Bắc Giang'), ('Khánh Hòa', 'Khánh Hòa'), ('Quảng Bình', 'Quảng Bình'), ('Gia Lai', 'Gia Lai'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Sơn La', 'Sơn La'), ('Thanh Hóa', 'Thanh Hóa'), ('Bà Rịa – Vũng Tàu', 'Bà Rịa – Vũng Tàu'), ('Đắk Lắk', 'Đắk Lắk'), ('Vĩnh Long', 'Vĩnh Long'), ('Tây Ninh', 'Tây Ninh'), ('Lào Cai', 'Lào Cai'), ('Hòa Bình', 'Hòa Bình'), ('Quảng Nam', 'Quảng Nam'), ('Phú Thọ', 'Phú Thọ'), ('Long An', 'Long An'), ('Hưng Yên', 'Hưng Yên'), ('Yên Bái', 'Yên Bái'), ('Lai Châu', 'Lai Châu'), ('Đắk Nông', 'Đắk Nông'), ('Bắc Kạn', 'Bắc Kạn'), ('Hà Giang', 'Hà Giang'), ('Đồng Nai', 'Đồng Nai'), ('Sóc Trăng', 'Sóc Trăng'), ('Bạc Liêu', 'Bạc Liêu'), ('An Giang', 'An Giang'), ('Cao Bằng', 'Cao Bằng'), ('Hậu Giang', 'Hậu Giang'), ('Tiền Giang', 'Tiền Giang'), ('Hải Phòng', 'Hải Phòng')], default='null', max_length=100),
        ),
    ]
