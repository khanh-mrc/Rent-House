from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('detail',views.detail,name='detail'),
    path('search',views.search,name='search'),
    path('test',views.test,name='test')
]