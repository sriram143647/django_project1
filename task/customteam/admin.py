from pyexpat import model
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth.admin import UserAdmin

from customteam.models import CustomTeam

# Register your models here.
@admin.register(CustomTeam)
class CustomTeamAdmin(admin.ModelAdmin):
    model = CustomTeam
    list_display = ['team_name','team_leader','members'] 
