from django.contrib import admin
from mini_blog.models import post

# Register your models here.
@admin.register(post)
class std_admin(admin.ModelAdmin):
    list_display = ['author','title','desc','publish_date']