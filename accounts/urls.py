from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from house.views import listing_dashboard



urlpatterns = [
    path('login/',views.loginPage,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('register/',views.register,name = "register"), 
    path('dashboard/',listing_dashboard,name="dashboard"),
    #path('dashboard/contacts',views.dashboard,name="contacts"),
    path('profile/',views.profile,name="profile"),
    path('profile/setting',views.profile_setting,name="profile_setting"),            
    #path('profile/changepwd',views.changepwd,name="changepwd"),
    path('profile/password_change', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name="password_change"),
    path('profile/favourites/', views.favourite_list, name='favourite_list'),
    path('fav/<str:pk>/', views.favourite_add, name='favourite_add'),
    
    path('reset_password', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_send', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
