from django.contrib import admin
from app1.models import student_data

# Register your models here.
@admin.register(student_data)
class std_admin(admin.ModelAdmin):
    list_display = ['id','uid','name','mail','gender','city']

# admin.site.register(student_data,std_admin)
# admin.site.register(student_data)