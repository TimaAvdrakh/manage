from django.contrib import admin
from django.contrib.auth.models import Permission

from apps.system import models


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AppModel)
class AppModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')


@admin.register(models.UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'kind', 'number', 'created_at', 'class_name')


@admin.register(models.AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_request', 'created_at')
