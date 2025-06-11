from django.urls import path
from .views import feedback_home

app_name = 'feedback'
urlpatterns = [
    path('', feedback_home, name='feedback_home'),
]
