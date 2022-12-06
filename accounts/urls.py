from django.urls import path
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.loginPage,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('register/',views.register,name = "register"), 
    path('dashboard/',views.dashboard,name="dashboard"),
    path('profile/',views.profile,name="profile"),
    path('profile/setting',views.profile_setting,name="profile_setting"),            
    #path('profile/changepwd',views.changepwd,name="changepwd"),
    path('profile/password_change', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name="password_change"),
]