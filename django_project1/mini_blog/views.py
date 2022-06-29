from django.http import HttpRequest as request
from django.http import HttpResponse as response
from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.utils.functional import SimpleLazyObject
from login_app.forms import signup_form,edit_user_profile,edit_admin_profile

# Create your views here.
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                user_fm = edit_admin_profile(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                user_fm = edit_user_profile(request.POST,instance=request.user)
            if user_fm.is_valid():
                messages.success(request,'Profile updated successfully')
                user_fm.save()
                return redirect('/miniblog/profile/')
        else:
            if request.user.is_superuser == True:
                user_fm = edit_admin_profile(instance=request.user)
                users = User.objects.all()
            else:
                user_fm = edit_user_profile(instance=request.user)
                users = None
        return render(request,'blog/profile.html',{'name':request.user,'user':user_fm,'users':users})
    else:
        return redirect('/miniblog/login/')

def user_logout(request):
    logout(request)
    return redirect('/miniblog/login/')

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            change_pass_fm = PasswordChangeForm(user=request.user, data=request.POST)
            if change_pass_fm.is_valid():
                change_pass_fm.save()
                update_session_auth_hash(request,change_pass_fm.user)
                messages.success(request,'password changed successfully')
                return redirect('/miniblog/profile/')
            else:
                pass
        else:
            change_pass_fm = PasswordChangeForm(user=request.user)
        return render(request,'login/change_pass.html',{'user':change_pass_fm})
    else:
        return redirect('/miniblog/login/')

def user_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            if not isinstance(request.user,SimpleLazyObject):
                return redirect('/miniblog/profile/')

    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            auth = AuthenticationForm(request=request, data=request.POST,auto_id=True,label_suffix='')
            if auth.is_valid():
                user_name = auth.cleaned_data['username']
                user_pass = auth.cleaned_data['password']
                auth_user = authenticate(request,username=user_name,password=user_pass)
                if auth_user is not None:
                    login(request,auth_user)
                    messages.success(request,'Logged in successfully!!')
                    return redirect('/miniblog/profile/')
        else:
            messages.success(request,"User doesn't exists, Please signup")
            auth = AuthenticationForm(auto_id=True,label_suffix='')
            return render(request,'blog/login.html',{'user':auth})
    else:
        auth = AuthenticationForm(auto_id=True,label_suffix='')
        return render(request,'blog/login.html',{'user':auth})
    return render(request,'blog/login.html',{'user':auth})

def sign_up(request):
    if request.method == 'POST':
        user = signup_form(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, f'New user is added successfully')
            user = signup_form()
    else:
        user = signup_form()
    return render(request,'blog/sign_up.html',{'user':user})

def user_detail(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        user_fm = edit_user_profile(instance=user)
        return render(request,'login/user_detail.html',{'user':user_fm})
    else:
        return redirect('/miniblog/profile/')

def blog_about(request):
    return render(request,'blog/about.html')

def blog_contact(request):
    return render(request,'blog/contact.html')

def blog_index(request):
    return render(request,'blog/index.html')