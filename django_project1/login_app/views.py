import re
from requests import request
from django import forms
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect as redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.
class signup_form(UserCreationForm):
    password2 = forms.CharField(label='Re-enter Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'E-mail'}
        
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'login/profile.html',{'name':request.user})
    else:
        messages.success(request,"User doesn't exist, Please sign up")
        return redirect('/loginapp/login/')

def user_logout(request):
    logout(request)
    return redirect('/loginapp/login/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            auth = AuthenticationForm(request=request, data=request.POST,auto_id=True,label_suffix='')        
            if auth.is_valid():
                user_name = auth.cleaned_data['username']
                user_pass = auth.cleaned_data['password']
                auth_user = authenticate(request,username=user_name,password=user_pass)
                if auth_user is not None:
                    login(request,auth_user)
                    messages.success(request,'Logged in successfully !!')
                    return redirect('/loginapp/profile/')
        else:
            auth = AuthenticationForm(auto_id=True,label_suffix='')
        return render(request,'login/login.html',{'user':auth})
    else:
        return redirect('/loginapp/profile/')        

def sign_up(request):
    if request.method == 'POST':
        user = signup_form(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, f'New user is added successfully')
            user = signup_form()
    else:
        user = signup_form()
    return render(request,'login/sign_up.html',{'user':user})        
    