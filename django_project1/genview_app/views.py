from django.shortcuts import render
from django.views.generic.list import ListView
from genview_app.models import student_detail

# Create your views here.
class std_listview(ListView):
    # default setting
    model = student_detail
    ordering = ['std_name']
    
    # custom setting
    template_name = 'genview_app/std_details.html'
    context_object_name = 'std_data'
    
    def get_queryset(self):
        return student_detail.objects.filter(std_mail__contains='gmail')
    
    def get_context_data(self, **kwargs):
        new_context = super().get_context_data(**kwargs)
        stds = new_context['object_list']
        std_datails = stds.order_by('std_name')
        new_context = {'std_data':std_datails}
        return new_context
    
    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         template_name = 'genview_app/superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'genview_app/staff.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]
        