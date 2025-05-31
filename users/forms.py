from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('guest', 'Гість'),
        ('parent', 'Батько/Мати'),
        ('teacher', 'Вчитель'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Роль')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')
