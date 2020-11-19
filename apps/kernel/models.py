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
