from django.urls import path

from . import views
from django.views import generic as generic_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
]