from django.contrib import admin
from .models import Material, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file')
    list_filter = ('category',)
    search_fields = ('title',)
