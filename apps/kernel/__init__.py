from django.utils.translation import ugettext_lazy as _

INTERCEPTION_STATE = (
    ('wait', _('WAIT')),
    ('error', _('ERROR')),
    ('completed', _('COMPLETED')),
    ('performed', _('PERFORMED')),
)

TASK_STATE = (
    ('active', _('ACTIVE_TASK')),
    ('deleted', _('DELETED_TASK')),
)

PERSONIDENTIFIER_KIND = (
    ('ip_address', _('PERSON_ID_KIND_IP_ADDR')),
    ('phone', _('PERSON_ID_KIND_PHONE')),
    ('account', _('PERSON_ID_KIND_ACC')),
    ('email', _('PERSON_ID_KIND_EMAIL')),
)
