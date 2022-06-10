import re
from attr import attrs
from django.core import validators
from django import forms
from app1.models import student_data

def check_name(val):
    if not val.isalpha():
        raise forms.ValidationError('Invalid Name please check.')
      
class std_register(forms.ModelForm):
    class Meta:
        model = student_data
        fields = ("std_id","std_name","std_mail","std_phone")
        labels = {'std_id':'ID','std_name':'Name','std_mail':'EMail-ID','std_phone':'Phone number'}
        error_messages={'std_id':{'required':'ID is a mandatory field'},
                        'std_name':{'required':'Name is a mandatory field'},
                        'std_mail':{'required':'E-mail is a mandatory field'},
                        'std_phone':{'required':'phone no. is a mandatory field'},
                    }
        widgets = {'std_id':forms.NumberInput(attrs={'placeholder':'Enter the ID'}),
                    'std_name':forms.TextInput(attrs={'placeholder':'Enter the Name'}),
                    'std_mail':forms.EmailInput(attrs={'placeholder':'Enter the Mail'}),
                    'std_phone':forms.TextInput(attrs={'placeholder':'Enter the Phone no'}),
                }
        
# class std_register(forms.Form):
#     std_phone_error_dict= {'required':'Phone no is mandatory field','max_length':'phone no is too long','min_length':'phone no is too short'}
#     std_name_error_dict= {'required':'Name is mandatory field','max_length':'Name is too long','min_length':'Name is too short'}

#     std_phone = forms.CharField(label='Phone No',min_length=10,max_length=15,error_messages=std_phone_error_dict)
#     std_id = forms.IntegerField(label='ID',error_messages={'required':'ID is a mandatory field'})
#     std_mail = forms.EmailField(label='E-Mail',error_messages={'required':'E-mail is a mandatory field'})
#     std_name = forms.CharField(label='Name',strip=True,error_messages=std_name_error_dict,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5),check_name])
      
#     # custom validator using 'clean'
#     # def clean_std_phone(self):
#     #     cleaned_data = super().clean()
#     #     phone = cleaned_data['std_phone']
#     #     regex = "^\\+?[1-9][0-9]{7,14}$"
#     #     if re.search(regex, phone):
#     #         return phone
#     #     else:
#     #         raise forms.ValidationError('Invalid Phone number please check.')