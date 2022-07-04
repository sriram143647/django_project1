from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from team.models import Team
from team.serializers import ReadTeamSerializers, WriteTeamSerializers

class TeamViewSet(ModelViewSet) :
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.action in ("get", "list") :
            return ReadTeamSerializers
        
        return WriteTeamSerializers


    
