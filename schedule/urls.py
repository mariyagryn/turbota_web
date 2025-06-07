from django.urls import path
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.schedule_home, name='schedule_home'),
]

