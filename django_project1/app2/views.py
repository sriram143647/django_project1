from django.shortcuts import render
from django.http import HttpResponse as response

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
        'profession':'Python developer',
        'hobby1':'Reading books',
        'hobby2':'Listening Music',
        'hobby3':'Travelling',
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
