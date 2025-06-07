from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # list_display: patronymic after last_name
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'patronymic', 'is_staff', 'is_active',
    )

    # fieldsets: patronymic after last_name in 'Personal info'
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # add_fieldsets: patronymic after last_name
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'patronymic', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
