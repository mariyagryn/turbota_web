from django.db import models

class News(models.Model):
    text = models.TextField('Текст новини')
    published_at = models.DateTimeField('Дата публікації', editable=True, blank=True, null=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    def __str__(self):
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
