from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def user_login(sender,request,user,**kwargs):
    print('user logged in successfully')
    print('---------------------------')
    print('Sender:',sender)
    print('Request:',request)
    print('User:',user)
    print('Password:',user.password)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
def user_logout(sender,request,user,**kwargs):
    print('user logged out successfully')
    print('---------------------------')
    print('Sender:',sender)
    print('Request:',request)
    print('User:',user)
    print(f'kwargs {kwargs}')
    print('---------------------------')
user_logged_out.connect(user_logout,sender=User)

@receiver(user_login_failed)
def user_login(sender,credentials,request,**kwargs):
    print('user login failed')
    print('---------------------------')
    print('Sender:',sender)
    print('Request:',request)
    print('credentials:', credentials)
    print(f'kwargs {kwargs}')
    print('---------------------------')