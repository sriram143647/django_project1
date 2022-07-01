from attr import fields
from rest_framework import serializers
from customtask.models import CustomTask
from customuser.models import CustomUser


class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomTask
        fields = '__all__'