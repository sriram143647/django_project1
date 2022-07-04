from django.db import models
from django.contrib.auth import models as auth_models

from django.conf import settings

# Create your models here.

class CustomUser(auth_models.AbstractUser) :
    
    department_name = models.CharField(max_length=45, null=True)

    def __str__(self) -> str:
        return f"{self.id} {self.first_name}"



