from django.shortcuts import render
from django.http import HttpResponse as response
from django.http import HttpResponseRedirect as redirect
from django.views import View
from django.views.generic.base import TemplateView
from app2.forms import std_register
from app1.models import student_data
from django.contrib import messages

###########################################################################################
# Create your views here.
class myview(View):
    name= 'ram'
    def get(self,request):
        return response(f'<h1>This is class based get view from user: {self.name}</h1>')
    
class myviewchild(myview):
    def get(self,request):
        return response(f'<h1>This is class based get child view from user: {self.name}</h1>')
    
################################################################################################

class homeview(TemplateView):
    template_name = 'home.html'
    # template_name = ''
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # context['fname'] = 'sriram'
        # context['lname'] = 'kusuma'
        # context['roll'] = 22
        context = {'fname':'sriram','lname':'kusuma','roll':22}
        return context
        
        
    # def get(self,request):
    #     # template_name = 'home.html'
    #     context = {'msg':'This message is printed to welcome you to site'}
    #     return render(request,self.template_name, context)
    
#################################################################################################

class formview(View):
    def get(self,request):
        std_frm = std_register(auto_id=True,label_suffix='')
        std_frm.order_fields(field_order=['uid','name','mail','phone'])
        return render(request,'app2_templates/student_register_form.html',{'std_form':std_frm})
    
    def post(self,request):
        std_frm = std_register(request.POST,auto_id=True,label_suffix='')
        if std_frm.is_valid():
            ins_id = std_frm.cleaned_data['uid']
            std_details = student_data.objects.all()
            for std in std_details:
                if ins_id == std.uid:
                    std_ins = student_data(instance=std)
                    std_ins.save()
                    messages.success(request, f'Record {ins_id} updated successfully')
                    return redirect('/app2/view_data/')
            else:
                std_frm.save()
                messages.success(request, f'New Record {ins_id} inserted successfully')
                return redirect('/app2/view_data/')
            
#################################################################################################