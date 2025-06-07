from django.urls import path
from . import views

app_name = 'materials'
urlpatterns = [
    path('', views.materials_home, name='materials_home'),
]
