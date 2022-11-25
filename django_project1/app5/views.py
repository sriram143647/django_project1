from django.shortcuts import render
from django.http import HttpResponse as response
from django.views import View

# Create your views here.
# def myview(request):
#     return response('<h1>This is function based view</h1>')

class myview(View):
    name= 'ram'
    def get(self,request):
        return response(f'<h1>This is class based get view from user: {self.name}</h1>')
    
class myviewchild(myview):
    def get(self,request):
        return response(f'<h1>This is class based get child view from user: {self.name}</h1>')