from django import forms
from customteam.models import CustomTeam

class MovieChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    genre = forms.ModelMultipleChoiceField(queryset=CustomTeam.objects.all(), required=False)
