from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.games_home, name='games_home'),
]
