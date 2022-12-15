from django.shortcuts import render

# Create your views here.
def get_profile(request):
    return render(request,'registration/profile.html')

