from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.games_home, name='games_home'),
    path('game1/', views.game1, name='game1'),
    path('game2/', views.game2, name='game2'),
    path('game3/', views.game3, name='game3'),
]
