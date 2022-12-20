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
from django.urls import path,include
from project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('app1/',include('app1.urls')),
    path('app2/',include('app2.urls')),
    path('app3/',include('app3.urls')),
    path('app5/',include('app5.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('custom_auth/',include('custom_auth_app.urls')),
    # path('accounts/',include('auth_app.urls')),
    # path('crud2/',include('crud_app2.urls')),
    # path('genview/',include('genview_app.urls')),
    # path('genform/',include('genview_form.urls')),
    # path('crud/',include('crud_app.urls')),
    # path('loginapp/',include('login_app.urls')),
    # path('miniblog/',include('mini_blog.urls')),
    # path('cache/',include('cache_api.urls')),
    # path('signal/',include('signal_app.urls')),
    # path('middleware/',include('middleware_app.urls')),
    path('proj/index/',views.index),
    path('proj/team/',views.team),
    path('proj/portfolio/',views.portfolio),
    path('proj/contact/',views.contact),
]