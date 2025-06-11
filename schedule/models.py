from django.db import models

# Models for schedule app. Add your models here.

class ScheduleFile(models.Model):
    title = models.CharField('Назва розкладу', max_length=200, default='Розклад занять')
    file = models.FileField('Файл розкладу', upload_to='schedule/')

    class Meta:
        verbose_name = 'Файл розкладу'
        verbose_name_plural = 'Файли розкладу'

    def __str__(self):
        return self.title
