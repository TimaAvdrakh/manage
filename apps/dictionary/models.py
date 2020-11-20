from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.system.models import TimestampMixin

ORG_KIND = (
    ('orm', _('ORG_ORM')),
    ('supervision', _('ORG_SUPERVISION'))
)


class Organization(TimestampMixin):
    class Meta:
        verbose_name = 'Органы ОРМ и надзора'
        verbose_name_plural = 'Органы ОРМ и надзора'
        permissions = (
            ('menu_view_organization', 'Органы ОРМ и надзора - в Меню'),
        )

    name = models.CharField(
        max_length=512,
        unique=True,
        verbose_name=_('organization_name')
    )
    kind = models.CharField(
        max_length=16,
        verbose_name=_('organization_kind'),
        choices=ORG_KIND
    )

    def __str__(self):
        return self.name
