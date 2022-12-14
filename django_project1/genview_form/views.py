from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from genview_form.forms import std_registration

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

class success_templateview(TemplateView):
    template_name = 'genview_form/success.html'
    
