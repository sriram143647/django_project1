from django.shortcuts import HttpResponse as response 
from django.template.response import TemplateResponse

# Create your views here.
def get_res(request):
    print('Middleware view is triggered')
    return response("This is view response triggered from middleware")

def get_excp(request):
    print('I am exception view')
    a = 10/0
    return response("This is exception view ")

def user_info(request):
    context = {'name':'rahul'}
    return TemplateResponse(request,'htmls/user.html',context)