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
from app2 import views

urlpatterns = [
    path('func1/',views.func1),
    path('func2/',views.func2),
    path('func3/',views.func3),
    path('func4/',views.func4),
    path('func5/',views.func5),
    path('temp2/',views.template2),
    path('proj/about/',views.app2_proj_about),
    path('proj/blog/',views.app2_proj_blog),
    path('proj/class/',views.app2_proj_class),
    path('proj/contact/',views.app2_proj_contact),
    path('proj/gallery/',views.app2_proj_gallery),
    path('proj/index/',views.app2_proj_index),
    path('proj/single/',views.app2_proj_single),
    path('proj/team/',views.app2_proj_team),
    path('register/',views.std_register_form),
    path('view_data/',views.student_detail,name='detail'),
]