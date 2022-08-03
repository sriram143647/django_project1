from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.core.signals import request_finished,request_started,got_request_exception
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import *
from django.db.backends.signals import connection_created
from django.core.cache import cache
from importlib_metadata import version

# login signals
@receiver(user_logged_in,sender=User)
def user_login(sender,request,user,**kwargs):
    print('user logged in successfully')
    print('---------------------------')
    # get client ip
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    print(ip)
    
    # login count
    ct = cache.get('count',0,version=user.pk)
    print(ct)
    new_count = ct +1
    cache.set('count',new_count,60*60*24, version=user.pk)    
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
def user_login_fai(sender,credentials,request,**kwargs):
    print('user login failed')
    print('---------------------------')
    print('Sender:',sender)
    print('Request:',request)
    print('credentials:', credentials)
    print(f'kwargs {kwargs}')
    print('---------------------------')

#model signals
@receiver(pre_save,sender=User)
def save_beginning(sender,instance,**kwargs):
    print('pre-save signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print('Instance:',instance)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
@receiver(post_save,sender=User)
def save_ending(sender,instance,created,**kwargs):
    if created:
        print('post-save signal waved')
        print('---------------------------')
        print('New Record Created')
        print('Sender:',sender)
        print('Instance:',instance)
        print('Created:',created)
        print(f'kwargs {kwargs}')
        print('---------------------------')
    else:
        print('post-save signal waved')
        print('---------------------------')
        print('Record Updated')
        print('Sender:',sender)
        print('Instance:',instance)
        print('Created:',created)
        print(f'kwargs {kwargs}')
        print('---------------------------')
        
@receiver(pre_delete,sender=User)
def delete_beginning(sender,instance,**kwargs):
    print('pre-delete signal waved')
    print('---------------------------')
    print('Record About to Deleted')
    print('Sender:',sender)
    print('Instance:',instance)
    print(f'kwargs {kwargs}')
    print('---------------------------')

@receiver(post_delete,sender=User)
def delete_ending(sender,instance,**kwargs):
    print('post-delete signal waved')
    print('---------------------------')
    print('Record Deleted')
    print('Sender:',sender)
    print('Instance:',instance)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
@receiver(pre_init,sender=User)
def init_beginning(sender,*args,**kwargs):
    print('pre-init signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print(f'args {args}')
    print(f'kwargs {kwargs}')
    print('---------------------------')

@receiver(post_init,sender=User)
def init_ending(sender,*args,**kwargs):
    print('post-init signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print(f'args {args}')
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
# request signals
@receiver(request_started)
def req_started(sender,environ,**kwargs):
    print('requested started signal')
    print('---------------------------')
    print('Sender:',sender)
    print('Enviroment:',environ)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
@receiver(request_finished)
def req_ended(sender,**kwargs):
    print('request ended signal')
    print('---------------------------')
    print('Sender:',sender)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
@receiver(got_request_exception)
def req_expect(sender,request,**kwargs):
    print('request exception signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print('request:',request)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
# management signals
@receiver(pre_migrate)
def before_migrations(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('pre migrate signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print('App config:',app_config)
    print('verbosity:',verbosity)
    print('Interactive:',interactive)
    print('Interactive:',interactive)
    print('Using:',using)
    print('Plan:',plan)
    print('Apps:',apps)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
@receiver(post_migrate)
def before_migrations(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('pre migrate signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print('App config:',app_config)
    print('verbosity:',verbosity)
    print('Interactive:',interactive)
    print('Interactive:',interactive)
    print('Using:',using)
    print('Plan:',plan)
    print('Apps:',apps)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    
# db signals
@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print('pre migrate signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print('Conn:',connection)
    print(f'kwargs {kwargs}')
    print('---------------------------')
    