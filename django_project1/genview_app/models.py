from django.db import models


# Create your models here.
class student_detail(models.Model):
    std_id = models.IntegerField()
    std_name = models.CharField(max_length=25)
    std_mail = models.EmailField(max_length=30)
    std_phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.std_name