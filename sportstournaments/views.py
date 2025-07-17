from rest_framework import generics
from .models import sportstournaments,teams,players,matches,matchresults
from .serializers import tournamentserializer,teamserializer,playerserializer,matchserializer,matcheresultserializer,Userserializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class tournamentlist(generics.ListCreateAPIView):
    queryset = sportstournaments.objects.all()
    serializer_class = tournamentserializer
    permission_classes =[IsAuthenticated]

class teamlist(generics.ListCreateAPIView):
    queryset = teams.objects.all()
    serializer_class=teamserializer
    permission_classes =[IsAuthenticated]

class playerlist(generics.ListCreateAPIView):
    queryset = players.objects.all()
    serializer_class=playerserializer
    permission_classes=[IsAuthenticated]

class matchlist(generics.ListCreateAPIView):
    queryset=matches.objects.all()
    serializer_class=matchserializer
    permission_classes=[IsAuthenticated]

class matchresultlist(generics.ListCreateAPIView):
    queryset=matchresults.objects.all()
    serializer_class=matcheresultserializer
    permission_classes=[IsAuthenticated]

class tournamentdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=sportstournaments.objects.all()
    serializer_class=tournamentserializer
    permission_classes=[IsAuthenticated]

class teamdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=teams.objects.all()
    serializer_class=teamserializer
    permission_classes=[IsAuthenticated]

class playerdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=players.objects.all()
    serializer_class=playerserializer
    permission_classes=[IsAuthenticated]

class matchesdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=matches.objects.all()
    serializer_class=matchserializer
    permission_classes=[IsAuthenticated]

class matchresultdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=matchresults.objects.all()
    serializer_class=matcheresultserializer
    permission_classes=[IsAuthenticated]

class Usercreate(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=Userserializer
