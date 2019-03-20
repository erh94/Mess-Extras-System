from django.shortcuts import render
from django.urls import path
# from accounts.views import UserLoginView, UserLogoutView
import guestBook.views as views
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', views.index,name='home'),
    path('login/',views.client_login,name='sso'),
    path('callback/',views.authenticated,name='callback'),
    path('entry/', views.LoginRequest, name='loggedIN'),
    # path('success/',views.index,name='success')
]