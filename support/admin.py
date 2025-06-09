from django.contrib import admin
from .models import Need, Help

@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'help_text')
    search_fields = ('name', 'phone', 'email', 'help_text')
