from django.db import models


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время последнего изменения'
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время удаления'
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name='Признак удаления'
    )


class AppModel(models.Model):
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    name = models.CharField(
        max_length=256,
        verbose_name='Наименование'
    )
    codename = models.CharField(
        max_length=32,

    )
    link = models.CharField(
        max_length=512,
        verbose_name='Ссылка',
        help_text='Вводится без указания хоста'
    )
    state = models.BooleanField(
        default=True,
        verbose_name='Состояние'
    )

#
# class AuditLog(TimestampMixin):
#     class Meta:
#         verbose_name = 'Журнал аудита'
#         verbose_name_plural = 'Журнал аудита'
#
