from django.shortcuts import render
from django.http import HttpResponse as response

# Create your views here.
def home(request):
    a = 'Homepage'
    return response(a)
    
def func1(request):
    a = 'This is Function 1 From app3'
    return response(a)

def func2(request):
    a = '<h1>This is Function 2 From app3 </h1>'
    return response(a)

def func3(request):
    a = '<h1><b>This is Function 3 From app3 </b></h1>'
    return response(a)

def func4(request):
    a = '<h1>This is Function 4 From app3 </h1>'
    return response(a)

def func5(request):
    a = '<h1>This is Function 5 From app3 </h1>'
    return response(a)

def template3(request):
    return render(request,'app3_templates/template_3.html')

def app3_proj_about(request):
    return render(request,'app3_proj_templates/about.html')

def app3_proj_blog(request):
    return render(request,'app3_proj_templates/blog.html')

def app3_proj_contact(request):
    return render(request,'app3_proj_templates/contact.html')

def app3_proj_index(request):
    return render(request,'app3_proj_templates/index.html')

def app3_proj_service(request):
    return render(request,'app3_proj_templates/service.html')