from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserCreationForm(UserCreationForm):
    patronymic = forms.CharField(label='По-батькові', max_length=150, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'patronymic' ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.patronymic = self.cleaned_data.get('patronymic', '')
        if commit:
            user.save()
            parent_group, created = Group.objects.get_or_create(name='parent')
            user.groups.add(parent_group)
        return user
