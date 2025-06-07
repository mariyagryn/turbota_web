from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Опікун'),
        ('teacher', 'Вчитель'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='parent')

    def is_teacher(self):
        return self.role == 'teacher'

    def is_parent(self):
        return self.role == 'parent'

    def __str__(self):
        return self.username
