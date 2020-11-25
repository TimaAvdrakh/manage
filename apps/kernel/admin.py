from django.contrib import admin

from apps.kernel import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FolderTask)
class FolderTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Sanction)
class SanctionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CommunicationObject)
class CommunicationObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'port', 'state')
    list_filter = ('state',)
