from django.db import models
from customuser.models import CustomUser

# Create your models here.
class CustomTeam(models.Model):
    team_name = models.CharField(max_length=25)
    
    team_leader = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='leader')
    team_members = models.ManyToManyField(CustomUser,related_name='member')
    
    def __str__(self):
        return self.team_name
    
    def members(self):
        return ",".join([str(m) for m in self.team_members.all()])