from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.system.models import TimestampMixin


class Organization(TimestampMixin):
    class Meta:
        verbose_name = 'Органы ОРМ и надзора'
        verbose_name_plural = 'Органы ОРМ и надзора'
        permissions = (
            ('menu_view_organization', 'Органы ОРМ и надзора - в Меню'),
        )

    name = models.CharField(
        max_length=512,
        verbose_name=_('organization_name')
    )

    def __str__(self):
        return self.name
