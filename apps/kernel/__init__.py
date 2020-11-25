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

