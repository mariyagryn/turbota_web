from django.db import models

class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']

    def __str__(self):
        return self.name

class Material(models.Model):
    title = models.CharField('Назва матеріалу', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='materials', verbose_name='Категорія')
    file = models.FileField('PDF-файл', upload_to='materials/')

    class Meta:
        verbose_name = 'Матеріал'
        verbose_name_plural = 'Матеріали'
        ordering = ['title']

    def __str__(self):
        return self.title
