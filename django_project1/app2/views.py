from django.shortcuts import render
from django.http import HttpResponse as response
from django.http import HttpResponseRedirect as redirect
from requests import request
from app2.forms import std_register

# Create your views here.
def home(request):
    a = 'Homepage'
    return response(a)
    
def func1(request):
    a = 'This is Function 1 From app2'
    return response(a)

def func2(request):
    a = '<h1>This is Function 2 From app2 </h1>'
    return response(a)

def func3(request):
    a = '<h1><b>This is Function 3 From app2 </b></h1>'
    return response(a)

def func4(request):
    a = '<h1>This is Function 4 From app2 </h1>'
    return response(a)

def func5(request):
    a = '<h1>This is Function 5 From app2 </h1>'
    return response(a)

def template2(request):
    bio_details = {
        'name':'Sriram',
        'city':'Surat',
        'hobby1':'Reading books',
        'hobby2':'Listening Music',
        'hobby3':'Travelling',
        'id':'',
        'mail_id':'',
        'phone':'',
    }
    return render(request,'app2_templates/template_2.html',bio_details)

def app2_proj_about(request):
    return render(request,'app2_proj_templates/about.html')

def app2_proj_blog(request):
    return render(request,'app2_proj_templates/blog.html')

def app2_proj_class(request):
    return render(request,'app2_proj_templates/class.html')

def app2_proj_contact(request):
    return render(request,'app2_proj_templates/contact.html')

def app2_proj_gallery(request):
    return render(request,'app2_proj_templates/gallery.html')

def app2_proj_index(request):
    return render(request,'app2_proj_templates/index.html')

def app2_proj_single(request):
    return render(request,'app2_proj_templates/single.html')

def app2_proj_team(request):
    return render(request,'app2_proj_templates/team.html')

def std_register_form(request):
    initial_val_dict = {
        'std_name':'Enter Name',
        'std_mail':'Enter Mail-id',
    }
    if request.method == 'POST':
        std_frm = std_register(request.POST,auto_id=True,label_suffix='',initial=initial_val_dict)
        if std_frm.is_valid():
            name = std_frm.cleaned_data['std_name']
            id = std_frm.cleaned_data['std_id']
            phone = std_frm.cleaned_data['std_phone']
            mail = std_frm.cleaned_data['std_mail']
            bio_details = {
                'name':name,
                'city':'Surat',
                'hobby1':'Reading books',
                'hobby2':'Listening Music',
                'hobby3':'Travelling',
                'id':id,
                'mail_id':mail,
                'phone':phone,
            }
            return render(request,'app2_templates/template_2.html',bio_details)
    else:
        std_frm = std_register(auto_id=True,label_suffix='',initial=initial_val_dict)
    std_frm = std_register(auto_id=True,label_suffix='',initial=initial_val_dict)
    std_frm.order_fields(field_order=['std_id','std_name','std_mail','std_phone'])
    return render(request,'app2_templates/student_register_form.html',{'std_form':std_frm})