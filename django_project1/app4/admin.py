from django.contrib import admin
from app4.models import father,mother,son,daughter

# Register your models here.
@admin.register(father)
class father_admin_mode(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','age','phone','salary']
    
@admin.register(mother)
class mother_admin_mode(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','age','phone','home_expenses']

@admin.register(son)
class son_admin_mode(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','age','phone','school_addr']
    
@admin.register(daughter)
class daughter_admin_mode(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','age','phone','school_addr']