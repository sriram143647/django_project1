from django.db import models
from customteam.models import CustomTeam


# Create your models here.
class CustomTask(models.Model):
    
    team_name = models.ForeignKey(CustomTeam,on_delete=models.CASCADE,null=True)

    task_name = models.CharField(max_length=50)
       
    TASK_CHOICES = [('P','Pending'),('I','In Progress'),('C','Completed')]
    status = models.CharField(max_length=1,choices=TASK_CHOICES,default='P')
    
    started_at = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    completed_at = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    
    def __str__(self):
        return self.task_name
    