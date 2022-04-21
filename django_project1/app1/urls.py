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
from app1 import views

urlpatterns = [
    path('func1/',views.func1),
    path('func1/',views.func2),
    path('func3/',views.func3),
    path('func4/',views.func4),
    path('func5/',views.func5),
    path('temp1/',views.template1),
    path('proj/index/',views.app1_proj_index),
    path('proj/about/',views.app1_proj_about),
    path('proj/clients/',views.app1_proj_clients),
    path('proj/contact/',views.app1_proj_contact),
    path('proj/ourwork/',views.app1_proj_ourwork),
]