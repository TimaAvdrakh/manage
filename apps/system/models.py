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


class UserRequest(TimestampMixin):
    class Meta:
        verbose_name = 'Запрос пользователя'
        verbose_name_plural = 'Запросы пользователя'

    user = models.ForeignKey(
        'userapp.MainUser',
        on_delete=models.PROTECT,
        verbose_name='Пользователь',
        null=True,
        blank=True
    )
    kind = models.CharField(
        max_length=10,
        verbose_name='Тип запроса',
        default='simple',
        choices=(
            ('simple', 'Простой'),
            ('foreign', 'Внешний'),
        )
    )
    class_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Имя класса'
    )
    number = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name='Номер запроса',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=16,
        default='new',
        verbose_name='Статус',
        choices=(
            ('new', 'Новый'),
            ('processing', 'В работе'),
            ('complete', 'Завершён'),
            ('error', 'Ошибка'),
        )
    )
    note = models.CharField(
        max_length=512,
        db_index=True,
        verbose_name='Заметка',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.number} - {self.kind}'


class AuditLog(TimestampMixin):
    class Meta:
        verbose_name = 'Журнал аудита'
        verbose_name_plural = 'Журнал аудита'

    user = models.ForeignKey(
        'userapp.MainUser',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Пользователь'
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )
    user_request = models.ForeignKey(
        'UserRequest',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Запрос пользователя'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    before = models.TextField(
        null=True,
        blank=True,
        verbose_name='До изменения'
    )
    after = models.TextField(
        null=True,
        blank=True,
        verbose_name='После изменения'
    )
