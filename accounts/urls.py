from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.loginPage,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('register/',views.register,name = "register"), 
    path('dashboard/',views.dashboard,name="dashboard")
]