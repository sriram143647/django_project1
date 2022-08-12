from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class family_comm_fields(models.Model):
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15) 
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(blank=True, validators=[MaxValueValidator(100)])
    dob = models.DateField()
    phone = models.IntegerField()
    home_addr = models.CharField(max_length=50)
    
    class Meta:
        abstract= True
    
class father(family_comm_fields):
    work_addr = models.CharField(max_length=50)
    salary = models.IntegerField(blank=True, validators=[MaxValueValidator(1000000)])
    
class mother(family_comm_fields):
    home_expenses = models.IntegerField(blank=True, validators=[MaxValueValidator(100000)])

class son(family_comm_fields):
    school_addr = models.CharField(max_length=50)
    pocket_money = models.IntegerField(blank=True, validators=[MaxValueValidator(5000)])
    
class daughter(family_comm_fields):
    school_addr = models.CharField(max_length=50)
    pocket_money = models.IntegerField(blank=True, validators=[MaxValueValidator(5000)])