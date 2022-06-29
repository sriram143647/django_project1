from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLES_CHOICES = [('U','User'),('L','Team Leader'),('M','Team Member')]
    roles = models.CharField(max_length=1,choices=ROLES_CHOICES,default='U')
    
    def __str__(self):
        return self.username
  

# class CustomTeam(models.Model):
#     team_name = models.CharField(max_length=25)
    
#     team_leader = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='leader')
#     team_members = models.ManyToManyField(CustomUser,related_name='member')
    
#     def __str__(self):
#         return self.team_name
    
# class CustomTask(CustomTeam):
#     task_name = models.CharField(max_length=50)
    
#     TASK_CHOICES = [('P','Pending'),('I','In Progress'),('C','Completed')]
#     status = models.CharField(max_length=1,choices=TASK_CHOICES,default='P')
    
#     started_at = models.DateField()
#     completed_at = models.DateField()
    
    # def __str__(self):
    #     return self.task_name
    