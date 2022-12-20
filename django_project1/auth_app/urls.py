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
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import path
# from auth_app import views
from auth_app.views import profileview,aboutview

urlpatterns = [
    # path('profile/',views.get_profile,name='profile'),
    # path('profile/',views.profileview.as_view(),name='profile'),
    path('profile/',login_required(profileview.as_view()),name='profile'),
    # path('about/',views.get_about,name='about')
    path('about/',aboutview.as_view(),name='about')
]