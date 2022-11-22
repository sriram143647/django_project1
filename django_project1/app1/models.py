from django.db import models
from app1.managers import CustomManager


# Create your models here.
class student_data(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=25)
    mail = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    link = models.URLField(max_length=100,blank=True)
    add1 = models.CharField(max_length=50,blank=True)
    add2 = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=10)
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    hobby1 = models.BooleanField('reading_books',default=False)
    hobby2 = models.BooleanField('travelling',default=False)
    hobby3 = models.BooleanField('listening_music',default=False)
    hobby4 = models.BooleanField('coding',default=False)
    hobby5 = models.BooleanField('sports',default=False)
    
    # built-in manager
    objects = models.Manager()
    
    # custom manager
    std_obj = CustomManager()
    
    
    def __str__(self):
        return self.name
    
class proxy_student_data(student_data):
    proxy_std_obj = CustomManager()
    class Meta:
        proxy = True
        ordering = ['name']