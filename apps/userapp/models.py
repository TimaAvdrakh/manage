from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.db import models

from apps.userapp.managers import MainUserManager

SENIOR_ADMIN = 'SENIOR_ADMIN'
HANDLER = 'HANDLER'
SUPERVISOR = 'SUPERVISOR'

ROLE_TYPES = (
    (SENIOR_ADMIN, _('SENIOR_ADMIN')),
    (HANDLER, _('HANDLER')),
    (SUPERVISOR, _('SUPERVISOR')),
)


class MainUser(AbstractBaseUser, PermissionsMixin):
    objects = MainUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        permissions = (
            ('menu_view_account', 'Учётные записи - в Меню'),
            ('menu_view_change_password', 'Смена пароля - в Меню'),
        )

    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=200, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=200, verbose_name=_('last_name'))
    role = models.CharField(
        max_length=20,
        verbose_name='Роль',
        choices=ROLE_TYPES
    )
    organization = models.ForeignKey(
        'dictionary.Organization',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Органы ОРМ и надзора'
    )
    folder = models.ForeignKey(
        'kernel.FolderTask',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Папка заданий'
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = []
