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
from genview_form import views

urlpatterns = [
    path('std_form/',views.std_formview.as_view(), name='std_form'),
    path('success/',views.success_templateview.as_view(), name='success'),
    path('std_create/',views.std_createview.as_view(), name='std_create'),
    path('std_update/<int:pk>/',views.std_updateview.as_view(), name='std_update'),
    path('update_success/',views.update_success_templateview.as_view(), name='success'),
    path('std_delete/<int:pk>/',views.std_deleteview.as_view(), name='std_delete'),
    path('delete_success/',views.delete_success_templateview.as_view(), name='success'),
    # path('std_detail/<int:pk>',views.student_detailview.as_view(), name='std_detail'),
]