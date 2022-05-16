from django import forms

class std_register(forms.Form):
    std_phone = forms.IntegerField(label='Phone-No')
    std_id = forms.IntegerField(label='ID')
    std_mail = forms.EmailField(max_length=30,label='E-Mail')
    std_name = forms.CharField(max_length=25,label='Name')
    

