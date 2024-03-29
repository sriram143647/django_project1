from django.db import models
from django.contrib.auth import get_user_model
from app1.models import student_data

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    content = models.TextField(max_length=1000)
    publish_date = models.DateField(null=True)
    # author = models.ForeignKey(get_user_model(), related_name="author", on_delete=models.CASCADE) 
    # author = models.OneToOneField(student_data, on_delete=models.CASCADE,primary_key=True)
    # author = models.OneToOneField(student_data, on_delete=models.PROTECT,primary_key=True)
    # author = models.OneToOneField(student_data, on_delete=models.CASCADE,primary_key=True, limit_choices_to={'is_staff':True})
    # author = models.ForeignKey(student_data, on_delete=models.CASCADE)
    # author = models.ForeignKey(student_data, on_delete=models.SET_NULL,null=True)
    author = models.ManyToManyField(student_data)
    
    def written_by(self):
        return ','.join([str(auth) for auth in self.author.all()])
    
# class like(post):
#     post_like = author = models.OneToOneField(post, on_delete=models.CASCADE,primary_key=True,parent_link=True)
#     likes = models.IntegerField()