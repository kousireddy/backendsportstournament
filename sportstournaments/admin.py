from django.contrib import admin
from .models import sportstournaments,teams,players,matches,matchresults

# Register your models here.
admin.site.register(sportstournaments)
admin.site.register(teams)
admin.site.register(players)
admin.site.register(matches)
admin.site.register(matchresults)