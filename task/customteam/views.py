from customteam.serializer import team_serializer
from customteam.models import CustomTeam
from rest_framework import viewsets

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = CustomTeam.objects.all()
    serializer_class = team_serializer