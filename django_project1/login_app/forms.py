from email.policy import default
from random import choices
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signup_form(UserCreationForm):
    password2 = forms.CharField(label='Re-enter Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'E-mail'}
        
    error_messages = {
        'phone':{'required':'Phone no is mandatory field','max_length':'phone no is too long','min_length':'phone no is too short'},
        'add1':{'required':'Address1 is mandatory field','max_length':'Address is too long'},
        'add2':{'max_length':'Address2 is too long'},
        'city':{'required':'City is mandatory field','max_length':'City Name is too long'},
        'gender':{'required':'Gender is mandatory field'}
    }
    
    phone = forms.CharField(label='Phone No',min_length=10,max_length=12)
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    add1 = forms.CharField(label='Address 1',max_length=50)
    add2 = forms.CharField(label='Address 2',max_length=50)
    city = forms.CharField(max_length=10)
    
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