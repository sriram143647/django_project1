from django.shortcuts import render
from django.http import HttpResponse as response
from django.db.models import Q
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
    # The following methods return new queryset
    # # retrieve data in objects 
    # std_details = student_data.objects.all()
    # std_details = student_data.objects.filter(gender='M')
    # std_details = student_data.objects.exclude(gender='M')
    # std_details = student_data.objects.order_by('uid')
    # std_details = student_data.objects.order_by('-uid')[:5]
    # std_details = student_data.objects.order_by('?')
    # std_details = student_data.objects.order_by('uid').reverse()[:6]
    
    # # retrieve data in dictionary
    # std_details = student_data.objects.values()
    # std_details = student_data.objects.values('uid','name')
    
    # # retrieve data in tuples
    # std_details = student_data.objects.values_list()
    # std_details = student_data.objects.values_list('uid','name')
    # std_details = student_data.objects.values_list('uid','name',named=True)
    
    # # db operation
    # std_details = student_data.objects.using('default')
    # # date operations
    # std_details = student_data.objects.dates('date_field','month',order='ASC')
    # std_details = student_data.objects.datetimes('datetime_field','month',order='ASC',tzinfo=None)
    
    # # None operation
    # std_details = student_data.objects.none()
    
    
    # qs1 = table1.objects.all()
    # qs2 = table2.objects.all()
    
    # # Union operation
    # std_details = qs2.union(qs1,all=True)
    
    # # Intersection operation
    # std_details = qs1.intersection(qs2)
    
    # # difference operation
    # std_details = qs1.difference(qs2)
    
    # The following methods return object
    # AND Operator
    # std_details = student_data.objects.filter(uid=104) & student_data.objects.filter(name='priya')
    # std_details = student_data.objects.filter(uid=104, name='priya')
    # std_details = student_data.objects.filter(Q(uid=104) & Q(name='priya'))
    
    # OR Operator
    # std_details = student_data.objects.filter(uid=114) | student_data.objects.filter(uid=107)
    std_details = student_data.objects.filter(Q(uid=114) | Q(uid=107))
    
    # query and result output
    print(f'sql query:{std_details.query}')
    return render(request,'app1_templates/student_details.html',{'stud_details':std_details})