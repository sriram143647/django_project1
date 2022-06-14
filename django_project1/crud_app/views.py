from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse as response
from django.http import HttpResponseRedirect as redirect
from requests import request
from crud_app.forms import std_registration
from crud_app.models import student_detail

# Create your views here.
def add_data(request):
    if request.method == 'POST':
        std_frm = std_registration(request.POST)
        if std_frm.is_valid():
            ins_name = std_frm.cleaned_data['std_name']
            ins_id = std_frm.cleaned_data['std_id']
            ins_phone = std_frm.cleaned_data['std_phone']
            ins_mail = std_frm.cleaned_data['std_mail']
            std_ins = student_detail(std_name = ins_name,std_id = ins_id,std_phone = ins_phone,std_mail = ins_mail)
            std_ins.save()
            std_frm = std_registration()
    else:
        std_frm = std_registration()
    std_details = student_detail.objects.all()
    std_frm.order_fields(field_order=['std_id','std_name','std_mail','std_phone'])
    return render(request,'crud/add_show.html',{'std_form':std_frm,'stud_details':std_details})

def update_data(request,id):
    if request.method == 'POST':
        std = student_detail.objects.get(pk=id)
        std_frm = std_registration(request.POST,instance=std)
        if std_frm.is_valid():
            std_frm.save()
            std_frm = std_registration()
            std_details = student_detail.objects.all()
            return render(request,'crud/add_show.html',{'std_form':std_frm,'stud_details':std_details})
    else:
        std = student_detail.objects.get(pk=id)
        std_frm = std_registration(instance=std)
        return render(request,'crud/update.html',{'std_form':std_frm})
    
def del_data(request,id):
    if request.method == 'POST':
        std = student_detail.objects.get(pk=id)
        std.delete()
        std_frm = std_registration()
        std_details = student_detail.objects.all()
        std_frm.order_fields(field_order=['std_id','std_name','std_mail','std_phone'])
        return render(request,'crud/add_show.html',{'std_form':std_frm,'stud_details':std_details})