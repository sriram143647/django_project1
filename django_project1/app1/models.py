from statistics import mode
from django.db import models
from django.forms import IntegerField

# Create your models here.

class student_data(models.Model):
    std_id = models.IntegerField()
    std_name = models.CharField(max_length=25)
    std_mail = models.EmailField(max_length=30)
    std_phone = models.IntegerField()
    std_info = models.CharField(max_length=100,default='please type something about you...')
    
    def __str__(self):
        return self.std_name