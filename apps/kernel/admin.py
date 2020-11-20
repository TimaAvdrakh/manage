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
