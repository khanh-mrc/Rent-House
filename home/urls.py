from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('dashboard',views.about,name='dashboard')
]