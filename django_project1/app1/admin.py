from django.contrib import admin
from app1.models import student_data

# Register your models here.
@admin.register(student_data)
class std_admin(admin.ModelAdmin):
    list_display = ['std_id','std_name','std_mail']

# admin.site.register(student_data,std_admin)
# admin.site.register(student_data)