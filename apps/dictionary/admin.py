from django.contrib import admin

from apps.dictionary import models


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
    list_filter = ('kind',)
