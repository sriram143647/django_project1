from django.shortcuts import render
from django.http import HttpResponse as response

# Create your views here.
def home(request):
    return render(request,'project_templates/home.html')

def index(request):
    return render(request,'project_templates/index.html')

def contact(request):
    return render(request,'project_templates/contact.html')

def team(request):
    return render(request,'project_templates/team.html')

def portfolio(request):
    return render(request,'project_templates/portfolio.html')