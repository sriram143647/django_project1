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
from django.contrib.auth import views as auth_views
from django.urls import path
from custom_auth_app.views import loginview,logoutview,changepassview,changepassdoneview
from custom_auth_app.forms import loginform

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'custom_auth_app/home.html')),
    path('index/',TemplateView.as_view(template_name = 'custom_auth_app/index.html')),
    # path("login/", auth_views.LoginView.as_view(template_name = 'custom_auth_app/login.html',authentication_form = loginform), name="login"),
    path("login/", loginview.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(template_name = 'custom_auth_app/logout.html'), name="logout"),
    path("logout/", logoutview.as_view(), name="logout"),
    # path("change_pass/", auth_views.PasswordChangeView.as_view(template_name = 'custom_auth_app/changepass.html',success_url='/custom_auth/change_pass_done/'), name="changepass"),
    path("change_pass/", changepassview.as_view(), name="changepass"),
    # path("change_pass_done/", auth_views.PasswordChangeDoneView.as_view(template_name = 'custom_auth_app/changepassdone.html'), name="changepassdone"),
    path("change_pass_done/", changepassdoneview.as_view(), name="changepassdone"),
]