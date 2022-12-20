from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
# @login_required
# def get_profile(request):
#     return render(request,'registration/profile.html')

# @login_required
# @staff_member_required
# def get_about(request):
#     return render(request,'registration/about.html')

class profileview(TemplateView):
    template_name = 'registration/profile.html'
    
# @method_decorator([login_required],name='dispatch')
@method_decorator([login_required,staff_member_required],name='dispatch')
class aboutview(TemplateView):
    template_name = 'registration/about.html'
    
    # @method_decorator(staff_member_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)