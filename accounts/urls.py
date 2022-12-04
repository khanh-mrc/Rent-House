from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.loginPage,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('register/',views.register,name = "register"), 
    path('dashboard/',views.dashboard,name="dashboard"),
    path('profile/',views.profile,name="profile"),
    path('profile/setting',views.profile_setting,name="profile_setting")
]