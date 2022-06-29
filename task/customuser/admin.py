from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customuser.forms import CustomUserCreationForm, CustomUserChangeForm
from customuser.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "first_name", "last_name", "email", "roles"]

admin.site.register(CustomUser, CustomUserAdmin)
