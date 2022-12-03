from django.urls import path
from django.contrib import admin
from . import views
from house.models import Listing

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('detail',views.detail,name='detail'),
    path('post',views.post,name='post'),
    
]