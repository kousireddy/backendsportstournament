from rest_framework import serializers
from .models import sportstournaments,teams,players,matches,matchresults
from django.contrib.auth.models import User

class tournamentserializer(serializers.ModelSerializer):
    class Meta:
        model = sportstournaments
        fields = '__all__'

class teamserializer(serializers.ModelSerializer):
    class Meta:
        model = teams
        fields = '__all__'

class playerserializer(serializers.ModelSerializer):
    class Meta:
        model = players
        fields = '__all__'

class matchserializer(serializers.ModelSerializer):
    class Meta:
        model = matches
        fields = '__all__'

class matcheresultserializer(serializers.ModelSerializer):
    class Meta:
        model = matchresults
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields =['username','password','email']
    
    def create(self, validated_data):
        user=User.objects.create_user(username=validated_data['username'],password=validated_data['password'],email=validated_data.get('email',''))
        return user


