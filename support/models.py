from django.db import models

# Models for support app. Add your models here.

class Need(models.Model):
    text = models.CharField('Потреба', max_length=255)

    class Meta:
        verbose_name = 'Потреба'
        verbose_name_plural = 'Потреби'
        ordering = ['id']

    def __str__(self):
        return self.text

class Help(models.Model):
    name = models.CharField('Імʼя', max_length=100)
    phone = models.CharField('Телефон', max_length=32, blank=True)
    email = models.EmailField('Email', blank=True)
    help_text = models.TextField('Допомога')

    class Meta:
        verbose_name = 'Волонтерська допомога'
        verbose_name_plural = 'Волонтерські допомоги'
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}: {self.help_text[:30]}"
