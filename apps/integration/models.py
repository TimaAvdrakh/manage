from django.db import models

from apps.system.models import TimestampMixin


class Session(TimestampMixin):
    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'

    id = models.CharField(primary_key=True, max_length=40)
    com_obj = models.ForeignKey(
        'kernel.CommunicationObject', on_delete=models.CASCADE,
    )
    state = models.CharField(max_length=10)
    params = models.CharField(max_length=512)


class RequestObject(TimestampMixin):
    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    id = models.BigAutoField(primary_key=True)
    session = models.ForeignKey(
        'Session',
        on_delete=models.CASCADE,
    )
    state = models.CharField(max_length=10)
    message_id = models.BigIntegerField(null=True, blank=True)
    message_time = models.CharField(max_length=20, null=True, blank=True)
    kind_id = models.IntegerField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)


class ResponseObject(TimestampMixin):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    id = models.BigAutoField(primary_key=True)
    session = models.ForeignKey(
        'Session',
        on_delete=models.CASCADE,
    )
    state = models.CharField(max_length=10)
    message_id = models.BigIntegerField(null=True, blank=True)
    message_time = models.CharField(max_length=20, null=True, blank=True)
    kind_id = models.IntegerField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
