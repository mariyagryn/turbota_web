from django.contrib import admin
from .models import ScheduleFile

@admin.register(ScheduleFile)
class ScheduleFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')

