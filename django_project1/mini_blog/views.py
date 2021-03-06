from django.http import HttpRequest as request
from django.http import HttpResponse as response
from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.functional import SimpleLazyObject
from django.views.decorators.cache import cache_page
from mini_blog.forms import signup_form,edit_user_profile,edit_admin_profile,loginform, PostForm
from mini_blog.models import post

# per-view caching is used in mini_blog
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
            auth = loginform(request=request, data=request.POST,auto_id=True,label_suffix='')
            if auth.is_valid():
                user_name = auth.cleaned_data['username']
                user_pass = auth.cleaned_data['password']
                auth_user = authenticate(request,username=user_name,password=user_pass)
                if auth_user is not None:
                    login(request,auth_user)
                    return redirect('/miniblog/dashboard/')
        else:
            messages.success(request,"User doesn't exists, Please signup")
            auth = loginform(auto_id=True,label_suffix='')
            return render(request,'blog/login.html',{'user':auth})
    else:
        auth = loginform(auto_id=True,label_suffix='')
        return render(request,'blog/login.html',{'user':auth})
    return render(request,'blog/login.html',{'user':auth})

def sign_up(request):
    if request.method == 'POST':
        user = signup_form(request.POST)
        if user.is_valid():
            usr = user.save()
            group = Group.objects.get(name='user')
            usr.groups.add(group)
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

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = PostForm(request.POST)
            if post.is_valid():
                post.save()
                messages.success(request, 'New post is added successfully')
                post = PostForm(auto_id=True,label_suffix='')
                return redirect('/miniblog/dashboard/')
        else:
            post = PostForm(auto_id=True,label_suffix='')
        return render(request,'blog/addpost.html',{'form':post})
    else:
        auth = loginform(auto_id=True,label_suffix='')
        return render(request,'blog/login.html',{'user':auth})

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_post = post.objects.get(pk=id)
            form = PostForm(request.POST,instance=user_post)
            if form.is_valid():
                form.save()
                return redirect('/miniblog/dashboard/')
        else:
            user_post = post.objects.get(pk=id)
            form = PostForm(instance=user_post)
            return render(request,'blog/addpost.html',{'form':form})
    else:
        auth = loginform(auto_id=True,label_suffix='')
        return render(request,'blog/login.html',{'user':auth})

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            del_post = post.objects.get(pk=id)
            del_post.delete()
            return redirect('/miniblog/dashboard/')
    else:
        auth = loginform(auto_id=True,label_suffix='')
        return render(request,'blog/login.html',{'user':auth})

@cache_page(180)    
def blog_about(request):
    return render(request,'blog/about.html')

@cache_page(180)
def blog_contact(request):
    return render(request,'blog/contact.html')

def blog_index(request):
    return render(request,'blog/index.html')

def blog_dashboard(request):
    if request.user.is_authenticated:
        posts = post.objects.all()
        full_name = request.user.get_full_name()
        return render(request,'blog/blog_dashboard.html',{'name':full_name,'posts':posts})
    else:
        auth = loginform(auto_id=True,label_suffix='')
        return render(request,'blog/login.html',{'user':auth})