# Generated by Django 4.1.4 on 2023-02-21 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0037_alter_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Cần Thơ', 'Cần Thơ'), ('Bến Tre', 'Bến Tre'), ('Bình Thuận', 'Bình Thuận'), ('Cà Mau', 'Cà Mau'), ('Hà Nội', 'Hà Nội'), ('Nghệ An', 'Nghệ An'), ('Tây Ninh', 'Tây Ninh'), ('Sơn La', 'Sơn La'), ('Bắc Kạn', 'Bắc Kạn'), ('Hậu Giang', 'Hậu Giang'), ('Quảng Nam', 'Quảng Nam'), ('Đồng Tháp', 'Đồng Tháp'), ('Gia Lai', 'Gia Lai'), ('Trà Vinh', 'Trà Vinh'), ('Lào Cai', 'Lào Cai'), ('Hà Nam', 'Hà Nam'), ('Bình Phước', 'Bình Phước'), ('Thừa Thiên Huế', 'Thừa Thiên Huế'), ('Hưng Yên', 'Hưng Yên'), ('Đắk Lắk', 'Đắk Lắk'), ('Yên Bái', 'Yên Bái'), ('Bà Rịa – Vũng Tàu', 'Bà Rịa – Vũng Tàu'), ('Ninh Thuận', 'Ninh Thuận'), ('Quảng Ninh', 'Quảng Ninh'), ('Thanh Hóa', 'Thanh Hóa'), ('Thái Nguyên', 'Thái Nguyên'), ('Cao Bằng', 'Cao Bằng'), ('Đà Nẵng', 'Đà Nẵng'), ('Hòa Bình', 'Hòa Bình'), ('Quảng Trị', 'Quảng Trị'), ('Phú Yên', 'Phú Yên'), ('Lâm Đồng', 'Lâm Đồng'), ('Điện Biên', 'Điện Biên'), ('Kiên Giang', 'Kiên Giang'), ('Vĩnh Phúc', 'Vĩnh Phúc'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Thái Bình', 'Thái Bình'), ('Bạc Liêu', 'Bạc Liêu'), ('Bình Dương', 'Bình Dương'), ('Kon Tum', 'Kon Tum'), ('Bắc Ninh', 'Bắc Ninh'), ('Ninh Bình', 'Ninh Bình'), ('Vĩnh Long', 'Vĩnh Long'), ('Đồng Nai', 'Đồng Nai'), ('An Giang', 'An Giang'), ('Hà Tĩnh', 'Hà Tĩnh'), ('Khánh Hòa', 'Khánh Hòa'), ('Tiền Giang', 'Tiền Giang'), ('Long An', 'Long An'), ('Nam Định', 'Nam Định'), ('TP. Hồ Chí Minh', 'TP. Hồ Chí Minh'), ('Bắc Giang', 'Bắc Giang'), ('Hải Dương', 'Hải Dương'), ('Lạng Sơn', 'Lạng Sơn'), ('Hà Giang', 'Hà Giang'), ('Quảng Bình', 'Quảng Bình'), ('Đắk Nông', 'Đắk Nông'), ('Bình Định', 'Bình Định'), ('Phú Thọ', 'Phú Thọ'), ('Hải Phòng', 'Hải Phòng'), ('Tuyên Quang', 'Tuyên Quang'), ('Sóc Trăng', 'Sóc Trăng'), ('Lai Châu', 'Lai Châu')], default='null', max_length=100),
        ),
    ]
