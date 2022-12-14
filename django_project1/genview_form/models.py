from django.db import models
from django.urls import reverse


# Create your models here.
class student_detail(models.Model):
    std_id = models.IntegerField()
    std_name = models.CharField(max_length=25)
    std_mail = models.EmailField(max_length=30)
    std_phone = models.CharField(max_length=10)
    
    # def get_absolute_url(self):
    #     return reverse("success")
    
    def get_absolute_url(self):
        return reverse("std_detail", kwargs={"pk": self.pk})
    
    
    
    def __str__(self):
        return self.std_name