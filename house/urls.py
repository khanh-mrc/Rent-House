from django.urls import path

from . import views

urlpatterns = [
    path('listings/',views.listing_list,name='listings'),
    path('search',views.search,name = "search"),
    path('listings/<int:listing_id>/', views.listing_retrieve, name='listing'),
    path('create/',views.listing_create,name='create'),
    path('update/<str:pk>',views.listing_update,name='update'),
    path('delete/<str:pk>',views.listing_delete,name='delete')
]   