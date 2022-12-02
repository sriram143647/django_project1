from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse as response
from django.http import HttpResponseRedirect as redirect
from requests import request
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from crud_app2.forms import std_registration
from crud_app2.models import student_detail

# Create your views here.
class add_std_data(TemplateView):
    template_name = 'crud/add_show.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        std_details = student_detail.objects.all()
        std_frm = std_registration()
        std_frm.order_fields(field_order=['std_id','std_name','std_mail','std_phone'])
        context = {'std_form':std_frm,'stud_details':std_details}
        return context
    
    def post(self, request):
        std_frm = std_registration(request.POST)
        if std_frm.is_valid():
            ins_name = std_frm.cleaned_data['std_name']
            ins_id = std_frm.cleaned_data['std_id']
            ins_phone = std_frm.cleaned_data['std_phone']
            ins_mail = std_frm.cleaned_data['std_mail']
            std_ins = student_detail(std_name = ins_name,std_id = ins_id,std_phone = ins_phone,std_mail = ins_mail)
            std_ins.save()
            return redirect('/crud2/app/')
            # std_frm = std_registration()
            # std_details = student_detail.objects.all()
            # std_frm.order_fields(field_order=['std_id','std_name','std_mail','std_phone'])
            # return render(request,'crud/add_show.html',{'std_form':std_frm,'stud_details':std_details})

class user_deleteview(RedirectView):
    url = '/crud2/app/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        student_detail.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    

class user_update_view(View):
    def get(self, request, id):
        std = student_detail.objects.get(pk=id)
        std_frm = std_registration(instance=std)
        return render(request,'crud/update.html',{'std_form':std_frm})
    
    def post(self,request, *args, **kwargs):
        del_id = kwargs['id']
        std = student_detail.objects.get(pk=del_id)
        std_frm = std_registration(request.POST,instance=std)
        if std_frm.is_valid():
            std_frm.save()
            return redirect('/crud2/app/')
            # return render(request,'crud/update.html',{'std_form':std_frm})