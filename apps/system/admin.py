from django.contrib import admin
from django.contrib.auth.models import Permission

from apps.system import models


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AppModel)
class AppModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'state')
