from django.urls import path
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.schedule_home, name='schedule_home'),
    path('edit/<int:pk>/', views.ScheduleFileUpdateView.as_view(), name='schedule_edit'),
]
