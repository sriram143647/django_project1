from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _

class signup_form(UserCreationForm):
    password2 = forms.CharField(label='Re-enter Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter the password Again'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter the password'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'E-mail'}
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter the User name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter the E-Mail'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Enter the First name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter the Last name'}),
        }

    phone = forms.CharField(label='Phone No',min_length=10,max_length=12,widget=forms.TextInput(attrs={'placeholder':'Enter the Phone no'}))
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    add1 = forms.CharField(label='Address 1',max_length=50,widget=forms.TextInput(attrs={'placeholder':'Enter the Address1'}))
    add2 = forms.CharField(label='Address 2',max_length=50,widget=forms.TextInput(attrs={'placeholder':'Enter the Address2'}))
    city = forms.CharField(label='City',max_length=10,widget=forms.TextInput(attrs={'placeholder':'Enter the City'}))
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