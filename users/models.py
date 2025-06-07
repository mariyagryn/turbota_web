from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomUser(AbstractUser):
    patronymic = models.CharField('По-батькові', max_length=150, blank=True)

    def is_teacher(self):
        return self.groups.filter(name='teacher').exists()

    def is_parent(self):
        return self.groups.filter(name='parent').exists()

    def is_admin(self):
        return self.is_superuser or self.groups.filter(name='admin').exists()

    def __str__(self):
        return self.username
