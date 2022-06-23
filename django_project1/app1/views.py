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
        if std.uid == my_id:
            hby_list = []
            if std.hobby1 == True:
                hby_list.append('Reading Books')
            if std.hobby2 == True:
                hby_list.append('Travelling')
            if std.hobby3 == True:
                hby_list.append('Listening Music')
            if std.hobby4 == True:
                hby_list.append('Coding')
            if std.hobby5 == True:
                hby_list.append('Sports')
            while True:
                if len(hby_list) < 3:
                    hby_list.append('')
                else:
                    break
            bio_details = {
                'name':std.name,
                'city':std.city,
                'hobby1':hby_list[0],
                'hobby2':hby_list[1],
                'hobby3':hby_list[2],
                'id':my_id,
                'mail_id':std.mail,
                'phone':std.phone,
                }
            return render(request,'app2_templates/template_2.html',bio_details)

def student_detail(request):
    std_details = student_data.objects.all()
    return render(request,'app1_templates/student_details.html',{'stud_details':std_details})