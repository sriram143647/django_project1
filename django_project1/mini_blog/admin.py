from django.contrib import admin
from mini_blog.models import post

# Register your models here.
@admin.register(post)
class std_admin(admin.ModelAdmin):
    list_display = ['written_by','title','desc','publish_date']

# @admin.register(like)
# class like_admin(admin.ModelAdmin):
#     list_display = ['author','title','desc','publish_date','like']