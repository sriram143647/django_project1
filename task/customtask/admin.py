from django.contrib import admin
from customtask.models import CustomTask

# Register your models here.
@admin.register(CustomTask)
class CustomTaskAdmin(admin.ModelAdmin):
    model = CustomTask
    list_display = ['task_name','team_name','status','started_at','completed_at']