from django.shortcuts import render


# Create your views here.


from rest_framework.viewsets import ModelViewSet
from task.permissions import IsUserRole, UserAllowedUpdate

from task.serializers import ReadTaskSerializer, CreateTaskSerializer, UpdateTaskSerializer
from .models import Task
from rest_framework import permissions


class TaskViewSet(ModelViewSet) :
    queryset = Task.objects.all()
    permission_classes = permissions.IsAuthenticated

    def get_serializer_class(self):
        if self.action in ("get", "list") :
            return ReadTaskSerializer
        elif self.action == "create" : 
            return CreateTaskSerializer
        return UpdateTaskSerializer

    def get_permissions(self):
        if self.action == "update" :
            return [permission() for permission in [permissions.IsAuthenticated, UserAllowedUpdate]]
        elif self.action == "create" :
             return [permission() for permission in [permissions.IsAuthenticated, IsUserRole]]
        
        return super().get_permissions()



    def create(self, request, *args, **kwargs):

        response = super().create(request, *args, **kwargs)
        
        # Send Mail From Celery
        
        return response
    




