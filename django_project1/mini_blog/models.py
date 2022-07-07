from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), related_name="author", on_delete=models.CASCADE) 