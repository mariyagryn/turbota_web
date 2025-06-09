from django.contrib import admin
from .models import Need

@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    search_fields = ('text',)

