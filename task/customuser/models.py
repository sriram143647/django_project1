from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLES_CHOICES = [('U','User'),('L','Team Leader'),('M','Team Member')]
    roles = models.CharField(max_length=1,choices=ROLES_CHOICES,default='U')
    
    def __str__(self):
        return self.username
    
