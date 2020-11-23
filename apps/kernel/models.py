from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.system.models import TimestampMixin


class FolderTask(TimestampMixin):
    class Meta:
        verbose_name = 'Папка заданий'
        verbose_name_plural = 'Папки заданий'

        permissions = (
            ('menu_view_folder_task', 'Папки заданий - в Меню'),
        )

    name = models.CharField(
        max_length=256,
        verbose_name=_('folder_task_name')
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        related_name='children',
        blank=True,
        verbose_name='Дочерние папки'
    )

    def __str__(self):
        return self.name


class Task(TimestampMixin):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

        permissions = (
            ('menu_view_task', 'Задания - в Меню'),
        )

    name = models.CharField(
        max_length=256,
        verbose_name=_('task_name')
    )

    def __str__(self):
        return self.name


class Sanction(TimestampMixin):
    class Meta:
        verbose_name = 'Санкция'
        verbose_name_plural = 'Санкции'

        permissions = (
            ('menu_view_sanction', 'Санкции - в Меню'),
            (
                'menu_view_sanction_interception',
                'Санкции - перехвата сообщений - в Меню'
            ),
            (
                'menu_view_sanction_information',
                'Санкции - служеюная информация - в Меню'
            ),
        )

    name = models.CharField(
        max_length=256,
        verbose_name=_('sanction_name')
    )

    def __str__(self):
        return self.name


class PersonIdentifiers(TimestampMixin):
    class Meta:
        verbose_name = 'Идентификатор абонента'
        verbose_name_plural = 'Идентификаторы абонентов'

        permissions = (
            (
                'menu_view_person_identifiers',
                'Идентификаторы абонентов - в Меню'
            ),
        )

    name = models.CharField(
        max_length=256,
        verbose_name=_('person_identifiers_name')
    )

    def __str__(self):
        return self.name
