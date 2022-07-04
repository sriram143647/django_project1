from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

class Team(models.Model) :

    name = models.CharField(max_length=45)
    leader = models.ForeignKey(get_user_model(), related_name="team", on_delete=models.CASCADE) 
    members = models.ManyToManyField(get_user_model(), related_name="related_team")

    def __str__(self) -> str:
        return f"{self.id} {self.name}"





