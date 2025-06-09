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
