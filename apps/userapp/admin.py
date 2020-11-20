from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.userapp import models


@admin.register(models.MainUser)
class MainUserAdmin(UserAdmin):
    list_display = ('identifier',)
    search_fields = ('identifier', 'first_name', 'last_name')
    ordering = ('-identifier',)
    fieldsets = (
        (
            None,
            {'fields': (
                'first_name', 'last_name', 'role', 'organization', 'folder'
            )}
        ),
        (
            'Password', {'fields': ('password',)}
        ),
        (
            'Permissions',
            {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups',
                        'user_permissions')}
        ),
    )
    add_fieldsets = (
        (
            None,
            {'fields': ('identifier', 'first_name', 'last_name', 'password1',
                        'password2')}
        ),
        (
            'Permissions',
            {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}
        ),
    )
