from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.system.models import TimestampMixin
from apps.kernel import (
    INTERCEPTION_STATE,
    TASK_STATE,
)


class CommunicationObject(TimestampMixin):
    class Meta:
        verbose_name = 'Объект связи'
        verbose_name_plural = 'Объекты связи'

        permissions = (
            ('menu_view_communication_objects', 'Объекты связи - в Меню'),
        )

    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    ip_address = models.GenericIPAddressField(
        verbose_name='IP адрес'
    )
    port = models.IntegerField(
        verbose_name='порт'
    )
    state = models.BooleanField(
        default=True,
        verbose_name='Статус'
    )

    def __str__(self):
        return self.name


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
    # organization = models.ForeignKey(
    #     'dictionary.Organization',
    #     on_delete=models.SET_NULL,
    #     related_name='task_organization',
    #     null=True,
    #     blank=True,
    #     verbose_name='Орган ОРМ или надзора'
    # )
    # folder_task = models.ForeignKey(
    #     'FolderTask',
    #     on_delete=models.SET_NULL,
    #     related_name='task_folder_task',
    #     null=True,
    #     blank=True,
    #     verbose_name='Папка заданий'
    # )
    # start_at = models.DateTimeField(
    #     null=True,
    #     blank=True,
    #     verbose_name='Дата/время начала перехвата'
    # )
    # stop_at = models.DateTimeField(
    #     null=True,
    #     blank=True,
    #     verbose_name='Дата/время окончания перехвата'
    # )
    # interception_state = models.CharField(
    #     max_length=16,
    #     default='wait',
    #     choices=INTERCEPTION_STATE,
    #     verbose_name='Статус перехвата'
    # )
    # task_state = models.CharField(
    #     max_length=16,
    #     default='active',
    #     choices=TASK_STATE,
    #     verbose_name='Статус задания'
    # )
    # communication_object = models.ManyToManyField(
    #     'CommunicationObject',
    #     through='TaskToCommunicationObject',
    #     verbose_name='Объекты связи'
    # )
    #
    # note = models.TextField(
    #     null=True,
    #     blank=True,
    #     verbose_name='Примечание'
    # )

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


## Services models

class TaskToCommunicationObject(models.Model):
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE
    )
    communication_object = models.ForeignKey(
        'CommunicationObject',
        on_delete=models.CASCADE
    )
