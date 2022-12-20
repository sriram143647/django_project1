from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from custom_auth_app.forms import loginform

class loginview(LoginView):
    template_name = 'custom_auth_app/login.html',
    authentication_form = loginform
    
class logoutview(LogoutView):
    template_name = 'custom_auth_app/logout.html'
    
class changepassview(PasswordChangeView):
    template_name = 'custom_auth_app/changepass.html',
    success_url='/custom_auth/change_pass_done/'
    
class changepassdoneview(PasswordChangeDoneView):
    template_name = 'custom_auth_app/changepassdone.html'