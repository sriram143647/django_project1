from django.db import models
from django import forms

# Create your models here.
class data_entry(models.Model):
    name = forms.CharField(max_length=50)
    dept = forms.CharField(max_length=50)
    info = forms.CharField(max_length=100)
    exercise_choice = [('Y','Yes'),('N','No')]
    Gender=forms.CharField(widget=forms.RadioSelect(choices=exercise_choice))
    topic_categories = (
        ('Books', 'Books'),
        ('online_resource', 'online_resource'),
        ('apps', 'apps'),
        ('magazines','magazines')
    )
    fav_topic_cat = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = topic_categories)
    
    