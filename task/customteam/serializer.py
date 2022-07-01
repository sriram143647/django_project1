from attr import fields
from rest_framework import serializers
from customteam.models import CustomTeam
from customuser.models import CustomUser


class team_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomTeam
        fields = '__all__'