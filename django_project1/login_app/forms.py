from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signup_form(UserCreationForm):
    password2 = forms.CharField(label='Re-enter Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'E-mail'}
        
class edit_user_profile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','last_login']
        labels = {'email':'E-mail'} 
        
class edit_admin_profile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'E-mail'} 