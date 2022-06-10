from django.db import models


# Create your models here.
class student_data(models.Model):
    std_id = models.IntegerField()
    std_name = models.CharField(max_length=25)
    std_mail = models.EmailField(max_length=30)
    std_phone = models.CharField(max_length=10)
    std_link = models.URLField(max_length=100,blank=True)
    def __str__(self):
            return self.std_name