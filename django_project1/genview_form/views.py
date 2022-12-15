from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from genview_form.forms import std_registration
from genview_form.models import student_detail
from django import forms

# Create your views here.
class std_formview(FormView):
    template_name = 'genview_form/std_form.html'
    form_class = std_registration
    success_url = '/genform/success/'
    # initial = {'std_name':'rakesh'}
    # def form_valid(self, form):
    #     name = form.cleaned_data['std_name']
    #     mail = form.cleaned_data['std_mail']
    #     return super().form_valid(form)

class std_createview(CreateView):
    # model = student_detail
    # fields = ("std_id","std_name","std_mail","std_phone")
    form_class = std_registration
    template_name = 'genview_form/std_form.html'
    success_url = '/genform/success/'
    
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'mypass'})
    #     return form

class success_templateview(TemplateView):
    template_name = 'genview_form/success.html'
    
# class student_detailview(DetailView):
#     model = student_detail

class std_updateview(UpdateView):
    model = student_detail
    fields = ("std_id","std_name","std_mail","std_phone")
    template_name = 'genview_form/std_form.html'
    success_url = '/genform/update_success/'
    
class update_success_templateview(TemplateView):
    template_name = 'genview_form/update_success.html'
    
class std_deleteview(DeleteView):
    model = student_detail
    success_url = '/genform/delete_success/'
    template_name = 'genview_form/confirm_del.html'
    
class delete_success_templateview(TemplateView):
    template_name = 'genview_form/delete_success.html'