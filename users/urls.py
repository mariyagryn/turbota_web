from django.urls import path
from .views import custom_login_view, register_view, parent_dashboard, teacher_dashboard, guest_dashboard

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', custom_login_view, name='login'),
    path('parent/', parent_dashboard, name='parent_dashboard'),
    path('teacher/', teacher_dashboard, name='teacher_dashboard'),
    path('guest/', guest_dashboard, name='guest_dashboard'),
]