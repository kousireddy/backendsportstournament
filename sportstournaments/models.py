from django.db import models

class sportstournaments(models.Model):
    name=models.CharField(max_length=200)
    sport=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    statdate=models.DateField()
    enddate=models.DateField()

    def __str__(self):
        return self.name

class teams(models.Model):
    name=models.CharField(max_length=200)
    couch=models.CharField(max_length=200)
    tid=models.ForeignKey(sportstournaments,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class players(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    position=models.CharField(max_length=200)
    teamid=models.ForeignKey(teams,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class matches(models.Model):
    tourid=models.ForeignKey(sportstournaments,on_delete=models.CASCADE)
    teamoneid=models.ForeignKey(teams,on_delete=models.CASCADE,related_name='teamone_matches')
    teamtwoid=models.ForeignKey(teams,on_delete=models.CASCADE,related_name='teamtwo_matches')
    matchdate=models.DateField()
    location=models.CharField(max_length=200)

class matchresults(models.Model):
    matchid=models.ForeignKey(matches,on_delete=models.CASCADE)
    teamonescore=models.IntegerField()
    teamtwoscore=models.IntegerField()
    winnerteamid=models.ForeignKey(teams,on_delete=models.CASCADE)