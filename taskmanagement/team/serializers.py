
from rest_framework import serializers

from team.models import Team
from user.serializers import CustomUserSerializer

class WriteTeamSerializers(serializers.ModelSerializer) :
    
    class Meta :
        model = Team
        fields = "__all__"

class ReadTeamSerializers(serializers.ModelSerializer) :
    
    leader = CustomUserSerializer()
    members = CustomUserSerializer(many = True)

    class Meta :
        model = Team
        fields = "__all__"


