from django import forms
from genview_app.models import student_detail

def check_name(val):
    if not val.isalpha():
        raise forms.ValidationError('Invalid Name please check.')
      
class std_registration(forms.ModelForm):
    class Meta:
        model = student_detail
        fields = ("std_id","std_name","std_mail","std_phone")
        labels = {'std_id':'ID','std_name':'Name','std_mail':'EMail-ID','std_phone':'Phone number'}
        error_messages={'std_id':{'required':'ID is a mandatory field'},
                        'std_name':{'required':'Name is a mandatory field'},
                        'std_mail':{'required':'E-mail is a mandatory field'},
                        'std_phone':{'required':'phone no. is a mandatory field'},
                }
        widgets = { 'std_id':forms.NumberInput(attrs={'placeholder':'Enter the ID'}),
                    'std_name':forms.TextInput(attrs={'placeholder':'Enter the Name'}),
                    'std_mail':forms.EmailInput(attrs={'placeholder':'Enter the Mail'}),
                    'std_phone':forms.TextInput(attrs={'placeholder':'Enter the Phone no'}),
                }