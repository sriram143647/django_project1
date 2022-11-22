from django.shortcuts import render
from django.http import HttpResponse as response
from django.db.models import Q,Avg,Sum,Max,Min,Count
from app1.models import student_data,proxy_student_data

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
    std_detail = student_data.std_obj.all()
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
    
    std_details = student_data.std_obj.all()
    
    # # retriev data from proxy model using custom manager
    # std_details = proxy_student_data.std_obj.all()
    # std_details = proxy_student_data.proxy_std_obj.get_stu_roll_range(102,108)
    
    # std_details = student_data.std_obj.filter(gender='M')
    # std_details = student_data.std_obj.exclude(gender='M')
    # std_details = student_data.std_obj.order_by('uid')
    # std_details = student_data.std_obj.order_by('-uid')[:5]
    # std_details = student_data.std_obj.order_by('?')
    # std_details = student_data.std_obj.order_by('uid').reverse()[:6]
    
    # # slicing
    # std_details = student_data.std_obj.all()[:5]
    # std_details = student_data.std_obj.all()[2:5]
    # std_details = student_data.std_obj.all()[1:10:2]
    
    # # retrieve data in dictionary
    # std_details = student_data.std_obj.values()
    # std_details = student_data.std_obj.values('uid','name')
    
    # # retrieve data in tuples
    # std_details = student_data.std_obj.values_list()
    # std_details = student_data.std_obj.values_list('uid','name')
    # std_details = student_data.std_obj.values_list('uid','name',named=True)
    
    # # db operation
    # std_details = student_data.std_obj.using('default')
    # # date operations
    # std_details = student_data.std_obj.dates('date_field','month',order='ASC')
    # std_details = student_data.std_obj.datetimes('datetime_field','month',order='ASC',tzinfo=None)
    
    # # None operation
    # std_details = student_data.std_obj.none()
    
    
    # qs1 = table1.std_obj.all()
    # qs2 = table2.std_obj.all()
    
    # # Union operation
    # std_details = qs2.union(qs1,all=True)
    
    # # Intersection operation
    # std_details = qs1.intersection(qs2)
    
    # # difference operation
    # std_details = qs1.difference(qs2)
    
    # The following methods return object
    # AND Operator
    # std_details = student_data.std_obj.filter(uid=104) & student_data.std_obj.filter(name='priya')
    # std_details = student_data.std_obj.filter(uid=104, name='priya')
    # std_details = student_data.std_obj.filter(Q(uid=104) & Q(name='priya'))
    
    # OR Operator
    # std_details = student_data.std_obj.filter(uid=114) | student_data.std_obj.filter(uid=107)
    # std_details = student_data.std_obj.filter(Q(uid=114) | Q(uid=107))
    
    # Not Operator
    # std_details = student_data.std_obj.filter(~Q(uid=114))

    # The following methods does not return new queryset
    # std_details = student_data.std_obj.get(uid=107)
    # std_details = student_data.std_obj.first()
    # std_details = student_data.std_obj.last()
    # std_details = student_data.std_obj.latest('mail')
    # std_details = student_data.std_obj.earliest('mail')
    # std_details = student_data.std_obj.order_by('name').first()
    # print(student_data.std_obj.filter(uid=105).exists())

    # record create method 1
    # s=student_data(uid='109',name='mayank',mail='mayank@gmail.com',gender='M',city='surat')
    # s.save(force_insert=True)
    
    # record create method 2
    # s = student_data.std_obj.create(uid='111',name='meena',mail='meena@gmail.com',gender='F',city='surat')
    
    # record create or get method
    # std_details,created = student_data.std_obj.get_or_create(uid='112',name='leela',mail='leela@gmail.com', gender='F', city='surat')
    
    # # record update method (it is applicable on queryset)
    # std_details = student_data.std_obj.filter(uid=112).update(phone='9966443322')
    
    # # record update or create method
    # std_details,created = student_data.std_obj.update_or_create(id=15,name='leela',defaults={'mail':'leela@yahoo.com'})
    
    # # records bulks create
    # std_objs = [
    #     student_data(uid='113',name='karan',mail='karan@gmail.com',phone='9944558877',gender='M',city='surat'),
    #     student_data(uid='114',name='riya',mail='riya@gmail.com',phone='9944223377',gender='F',city='surat'),
    #     student_data(uid='115',name='mohit',mail='mohit@gmail.com',phone='7744558877',gender='M',city='surat')
    # ]
    # std_details = student_data.std_obj.bulk_create(std_objs)
    
    # # records bulks update
    # std_data = student_data.std_obj.all()
    # for st in std_data:
    #     st.city = 'Surat'
    # std_details = student_data.std_obj.bulk_update(std_data,['city'])
    
    # The in_bulk method gives object data in bulk based on id
    # data = student_data.std_obj.in_bulk([5,8])
    
    # # retrun empty list
    # data = student_data.std_obj.in_bulk()
    
    # # retrun full dataset
    # data = student_data.std_obj.in_bulk()
    # print(data)
    
    # # bulk delete
    # std_details = student_data.std_obj.filter(name='saloni').delete()
    
    # # deelte all records
    # std_details = student_data.std_obj.all().delete()
    
    # # count records
    # dataset = student_data.std_obj.all()
    # print(dataset.count())
    
    # # vlookup operations
    # # prefix i for case insensitive operations
    # std_details = student_data.std_obj.filter(city__exact='Surat')
    # std_details = student_data.std_obj.filter(city__iexact='surat')
    # std_details = student_data.std_obj.filter(city__contains='Surat')
    # std_details = student_data.std_obj.filter(city__icontains='surat')
    # std_details = student_data.std_obj.filter(city__startswith='surat')
    # std_details = student_data.std_obj.filter(city__istartswith='surat')
    # std_details = student_data.std_obj.filter(city__endswith='surat')
    # std_details = student_data.std_obj.filter(city__iendswith='surat')
    # std_details = student_data.std_obj.filter(uid__in=[104,105,106])
    # std_details = student_data.std_obj.filter(city__gt=100)
    # std_details = student_data.std_obj.filter(city__gte=100)
    # std_details = student_data.std_obj.filter(city__lt=100)
    # std_details = student_data.std_obj.filter(city__lte=100)
    # std_details = student_data.std_obj.filter(uid__range=(104,110)
    # std_details = student_data.std_obj.filter(submit_date__date=(2022,10,12)
    # std_details = student_data.std_obj.filter(submit_date__date__gt=(2022,10,12)
    
    # # aggerate fucntion
    # avg = std_details.aggregate(Avg('marks'))
    # sum = std_details.aggregate(Sum('marks'))
    # max = std_details.aggregate(Max('marks'))
    # min = std_details.aggregate(Min('marks'))
    # count = std_details.aggregate(Count('marks'))
    # {'stud_details':std_details,'average':avg}
    print('operation performed successfully')
    # query and result output
    # print(f'sql query:{std_details.query}')
    # std_details = ''
    return render(request,'app1_templates/student_details.html',{'stud_details':std_details})