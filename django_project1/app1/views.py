from django.shortcuts import render
from django.http import HttpResponse as response
from app1.models import student_data

# Create your views here. 
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
    return render(request,'app1_templates/template_1.html')

def app1_proj_index(request):
    return render(request,'app1_proj_templates/index.html')

def app1_proj_about(request):
    return render(request,'app1_proj_templates/about.html')    

def app1_proj_clients(request):
    return render(request,'app1_proj_templates/clients.html',)

def app1_proj_contact(request):
    return render(request,'app1_proj_templates/contact.html')

def app1_proj_ourwork(request):
    return render(request,'app1_proj_templates/ourwork.html')

def show_data(request,my_id=0):
    std_detail = student_data.objects.all()
    for std in std_detail:
        if std.std_id == my_id:
            name = std.std_name
            mail = std.std_mail
            phone = std.std_phone
            bio_details = {
            'name':name,
            'city':'Surat',
            'hobby1':'Reading books',
            'hobby2':'Listening Music',
            'hobby3':'Travelling',
            'id':my_id,
            'mail_id':mail,
            'phone':phone,
            }
            return render(request,'app2_templates/template_2.html',bio_details)

def student_detail(request):
    std_details = student_data.objects.all()
    return render(request,'app1_templates/student_details.html',{'stud_details':std_details})