from django.shortcuts import render
from django.http import HttpResponse as response

# Create your views here.
def home(request):
    request.session['name']='sriram123'
    request.session.set_expiry(3600)
    res = render(request,'project_templates/home.html')
    # res.set_cookie(key='name',value='sriram',max_age=360,domain='http://127.0.0.1:8000/',secure=True,httponly=True,samesite='Strict')
    # res.set_signed_cookie(key='name',value='sriram',salt='abc@123',max_age=360,domain='http://127.0.0.1:8000/',secure=True,httponly=True,samesite='Strict')
    return res

def  get_session(request):
    name = request.session['name']
    if 'name' in request.session:
        # request.session.modified = True
        # print(request.session.keys())
        # print(request.session.items())
        # print(request.session.get_session_cookie_age())
        # print(request.session.get_expiry_age())
        # print(request.session.get_expiry_date())
        # print(request.session.get_expire_at_browser_close())
        # fname = request.session.setdefault('fname','kusuma')
        return render(request,'get_session.html',{'name':name})
    else:
        return response("Your Sessin has Expired.....")
    
def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request,'del_session.html')

def index(request):
    return render(request,'project_templates/index.html')

def contact(request):
    return render(request,'project_templates/contact.html')

def team(request):
    return render(request,'project_templates/team.html')

def portfolio(request):
    return render(request,'project_templates/portfolio.html')