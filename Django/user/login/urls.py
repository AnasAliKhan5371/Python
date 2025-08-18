from django.contrib import admin
from django.urls import path,include
from login import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),

    path('login/', auth_views.LoginView.as_view(template_name='log.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register'), name='logout'),

    path('home/', views.home, name='home')

]
