from django.apps import AppConfig


class MiniBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mini_blog'
    
    def ready(self):
       import mini_blog.signals