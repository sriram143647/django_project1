from django.dispatch import receiver,Signal

# custom signal
notify = Signal()

# custom receiver
@receiver(notify)
def notify_user(sender,**kwargs):
    print('custom signal waved')
    print('---------------------------')
    print('Sender:',sender)
    print(f'kwargs {kwargs}')
    print('---------------------------')

