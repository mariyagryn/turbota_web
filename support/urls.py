from django.urls import path
from . import views

app_name = 'support'
urlpatterns = [
    path('', views.support_home, name='support_home'),
    path('volunteer_form/', views.volunteer_form, name='volunteer_form'),
]
