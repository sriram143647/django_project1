from customtask.serializer import task_serializer
from customtask.models import CustomTask
from rest_framework import viewsets

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = CustomTask.objects.all()
    serializer_class = task_serializer