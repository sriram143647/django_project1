from ensurepip import version
from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
# def home(request):
#     mv = cache.get('movie','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','movie11',30)
#         mv.get('movie')
#     return render(request,'home.html')

# def home(request):
#     dt = cache.get_or_set('fees',30000,30,version=2)
#     return render(request,'home.html',{'data':dt})

# def home(request):
#     data = {'name':'ram','age':25}
#     cache.set_many(data,30,version=1)
#     dt = cache.get_many(data)
#     return render(request,'home.html',{'data':dt})

def home(request):
    cache.delete('age',version=1)
    return render(request,'home.html')