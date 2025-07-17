from django.urls import path
from .views import tournamentlist,teamlist,playerlist,matchlist,matchresultlist,tournamentdetail,playerdetail,teamdetail,matchesdetail,matchresultdetail,Usercreate
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/',Usercreate.as_view(),name='user-create'),
    path('token/',TokenObtainPairView.as_view(),name='get-token'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh-token'),
    path('tournament/',tournamentlist.as_view(),name='tournament-list'),
    path('tournament/<int:pk>',tournamentdetail.as_view(),name='tournament-detail'),
    path('teams/',teamlist.as_view(),name='team-list'),
    path('teams/<int:pk>',teamdetail.as_view(),name='team-detail'),
    path('players/',playerlist.as_view(),name='player-list'),
    path('players/<int:pk>',playerdetail.as_view(),name='player-detail'),
    path('matches/',matchlist.as_view(),name='match-list'),
    path('matches/<int:pk>',matchesdetail.as_view(),name='matches-detail'),
    path('matchresults/',matchresultlist.as_view(),name='matchresult-list'),
    path('matchresults/<int:pk>',matchresultdetail.as_view(),name='matchresult-detail')
]