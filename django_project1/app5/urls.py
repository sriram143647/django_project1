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
from django.urls import path
from app5 import views

urlpatterns = [ 
    # path('func/',views.myview, name='func'),
    # path('clview/',views.myview.as_view(), name='clview'),
    # path('clview/',views.myview.as_view(name='sriram'), name='clview'),
    # path('subclview/',views.myviewchild.as_view(), name='subclview'),
    path('homeview/',views.homeview.as_view(extra_context= {'course':'python'}), name='homeview'),
    path('homeview/<int:cl>',views.homeview.as_view(), name='cl_homeview'),
    path('formview/',views.formview.as_view(), name='formview'),
    # redirect urls
    # path('redirect_view/',views.RedirectView.as_view(url='/app5/homeview/'), name='red_homeview'),
    # path('redirect_view/',views.redirect_view.as_view(), name='red_view')
    path('redirect_view/',views.RedirectView.as_view(pattern_name='formview'),name='red_view'),
    # path('redirect_view/',views.redirect_view.as_view(), name='red_view')
]