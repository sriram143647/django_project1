from django.contrib import admin

from team.models import Team

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin) :

    class Meta :
        model = Team