from django.http import HttpResponse as response

class site_down:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        res = response('Site is Under Maintenace, Please come after sometime')
        return res  