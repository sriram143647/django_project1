from re import template
from django.shortcuts import render
from django.http import HttpResponse as response

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def func1(request):
    a = 'This is Function 1 From app1'
    return response(a)

def func2(request):
    a = '<h1>This is Function 2 From app1 </h1>'
    return response(a)

def func3(request):
    a = '<h1><b>This is Function 3 From app1 </b></h1>'
    return response(a)

def func4(request):
    a = '<h1>This is Function 4 From app1 </h1>'
    return response(a)

def func5(request):
    a = '<h1>This is Function 5 From app1 </h1>'
    return response(a)

def template1(request):
    return render(request,'template_1.html')

def template2(request):
    return render(request,'template_2.html')

def template3(request):
    return render(request,'template_3.html')