import datetime
from rest_framework import serializers

from task.models import Task
from team.serializers import ReadTeamSerializers
from user.serializers import CustomUserSerializer


class ReadTaskSerializer(serializers.ModelSerializer) :
    members = CustomUserSerializer(many = True)
    team = ReadTeamSerializers()
    
    class Meta :
        model = Task
        fields = "__all__"


class CreateTaskSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Task
        fields = ["name", "team"]
    

class UpdateTaskSerializer(serializers.ModelSerializer) :

    '''
    Lead Can Update Anything
    Members Can Update Status Only
    '''

    class Meta :
        model = Task
        fields = "__all__"


    def update(self, instance, validated_data):
        
        if "status" in validated_data and (validated_data['status'] == Task.STATUS_ASSIGNED) and (instance.staus == Task.STATUS_UNDER_REVIEW):
            validated_data['started_at'] = datetime.datetime.now()
        
        if "status" in validated_data and (validated_data['status'] == Task.STATUS_COMPLETED) and (instance.staus == Task.STATUS_IN_PROGRESS) :
            validated_data['completed_at'] = datetime.datetime.now()


        return super().update(instance, validated_data)

