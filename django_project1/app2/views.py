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