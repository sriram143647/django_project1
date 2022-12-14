from django.contrib import admin
from genview_form.models import student_detail

# Register your models here.
@admin.register(student_detail)
class std_admin(admin.ModelAdmin):
    list_display = ['id','std_id','std_name','std_mail']