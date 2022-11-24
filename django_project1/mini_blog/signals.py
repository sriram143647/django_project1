from app1.models import student_data
from mini_blog.models import post
from django.db.models.signals import post_delete
from django.dispatch import receiver

# @receiver(post_delete,sender=post)
# def del_related_user(sender,instance,**kwargs):
#     print('student user is deleted')
#     instance.author.delete()
#     pass