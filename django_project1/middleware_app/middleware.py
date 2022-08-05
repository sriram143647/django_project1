from django.http import HttpResponse as response

# # function based middleware
# def my_middleware(get_response):1
#     print('One Time Initilization code executed')
#     def my_function(request):
#         print('code before view execution')
#         res = get_response(request)
#         print('code after view execution')
#         return res
#     return my_function


# class based middleware
# middleware hooks are used along with class-based middleware only
class my_middleware1:
    def __init__(self,get_response):
        print('One Time Initilization or configuration code executed of middleware1') 
        self.get_response = get_response
        
    def __call__(self, request):
        print('middleware1 code before view execution or call middleware in chain of line')
        res = self.get_response(request)
        print('code after view execution')
        return res
    
# class based middleware
class my_middleware2:
    def __init__(self,get_response):
        print('One Time Initilization or configuration code executed of middleware3') 
        self.get_response = get_response
        
    def __call__(self, request):
        print('middleware2 code before view execution or call middleware in chain of line')
        # res = response('code execution is terminated at middleware2')
        res = self.get_response(request)
        print('code after view execution')
        return res
    
# class based middleware
class my_middleware3:
    def __init__(self,get_response):
        print('One Time Initilization or configuration code executed of middleware3') 
        self.get_response = get_response
        
    def __call__(self, request):
        print('middleware2 code before view execution or call middleware in chain of line')
        res = self.get_response(request)
        print('code after view execution')
        return res
    
class middleware_hook:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        res = self.get_response(request)
        return res
    
    def process_view(request,*agrs,**kwargs):
        print('process view is executed before main view')
        # return response('middleware process view is triggered before main view is executed')
        return None
    
    def process_exception(self,request,exception):
        print('exception occured')
        msg = exception
        return response(msg)
    
    def process_template_response(self,request,res):
        print('tempalte process response trigged from middleware')
        # res.context_data['name'] = 'ram'
        return res