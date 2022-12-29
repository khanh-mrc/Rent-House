# Nhóm 15 - Web Tìm Nhà Trọ 
#### Nembers: 
- 20521295	Trần Anh Hào
- 20521095	Bùi Chí Bảo 
- 20521456	Phạm Văn Khánh 
- 20521093	Trần Gia Băng 
-------------------------------------------------
- Deploy:  [Rental House](https://rentalhouse.up.railway.app/)
- Database: Postgresql : using live server https://console.neon.tech/ 
- Media upload: Cloudinary
----------------------------------------------- 
##### Super user:  
    * usr: admins 
    * pwd: admin 
------------------- 
##### Install venv-django:  
```
py -3 -m venv .venv  
.venv\scripts\activate 
python -m pip install django 
```

##### Install Lib: 
```
pip install Pillow 
pip install django-crispy-forms 
pip install psycopg2 
pip install django_cloudinary_storage 
```
##### Run:
```
python manage.py runserver
```