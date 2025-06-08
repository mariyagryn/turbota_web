from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('published_at', 'text')
    list_filter = ('published_at',)
    search_fields = ('text',)
    ordering = ('-published_at',)
    # Allow editing published_at in admin
    fields = ('text', 'published_at')
    readonly_fields = ()
