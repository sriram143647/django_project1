from django.urls import path
from customuser.views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]