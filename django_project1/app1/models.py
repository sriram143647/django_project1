from django.db import models


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
    
    def __str__(self):
            return self.name