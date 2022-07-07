"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mini_blog import views

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('index/',views.blog_index,name='index'),
    path('about/',views.blog_about,name='about'),
    path('contact/',views.blog_contact,name='contact'),
    path('addpost/',views.add_post,name='addpost'),
    path('updatepost/<int:id>',views.update_post,name='updatepost'),
    path('dashboard/',views.blog_dashboard,name='dashboard'),
    path('changepass/',views.user_change_pass,name='change_pass'),
    path('userdetail/<int:id>',views.user_detail,name='usrdetail'),
]