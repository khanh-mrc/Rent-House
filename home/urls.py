from django.urls import path
from django.contrib import admin
from . import views
from house.models import Listing

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('detail',views.detail,name='detail'),
    path('test',views.test,name='test'),
    path('post',views.post,name='post'),
    path('listing',views.listing,name = "listing"),
    path('listing/index',views.testsearch,name='testsearch'),
]