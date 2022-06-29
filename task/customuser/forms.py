from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from customuser.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "roles")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "roles")
        
        
# class CreateTaskForm(forms.ModelForm):
#     class Meta:
#         model = CustomTask
#         fields = ("task_name","status","team","team_members","started_at","completed_at")
        
# class CreateTeamForm(forms.ModelForm):
#     class Meta:
#         model = CustomTask
#         fields = ("team_name","team_leader","team_members")