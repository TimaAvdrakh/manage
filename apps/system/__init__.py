from django.utils.translation import ugettext_lazy as _

MENU_ITEMS = {
    'menu_view_organization': {
        'priority': 10,
        'name': _('menu_view_organization'),
        'link': '/organizations/',
    },
    'menu_view_account': {
        'priority': 20,
        'name': _('menu_view_account'),
        'link': '/accounts/',
    },
    'menu_view_folder_task': {
        'priority': 30,
        'name': _('menu_view_folder_task'),
        'link': '/folder_task/',
    },
    'menu_view_task': {
        'priority': 40,
        'name': _('menu_view_task'),
        'link': '/task/',
    },
    'menu_view_sanction': {
        'priority': 50,
        'name': _('menu_view_sanction'),
        'link': '/sanction/',
        'children': {
            'menu_view_sanction_interception': {
                'priority': 53,
                'name': _('menu_view_sanction_interception'),
                'link': '/sanction/interception/',
            },
            'menu_view_sanction_information': {
                'priority': 55,
                'name': _('menu_view_sanction_information'),
                'link': '/sanction/information/',

            },
        },
    },
    'menu_view_equipment': {
        'priority': 60,
        'name': _('menu_view_sanction'),
        'link': '/sanction/',
    },
    'menu_view_journal': {
        'priority': 70,
        'name': _('menu_view_journal'),
        'link': '/journal/',
    },
    'menu_view_person_identifiers': {
        'priority': 80,
        'name': _('menu_view_person_identifiers'),
        'link': '/person_identifiers/',
    },
    'menu_view_communication_objects': {
        'priority': 90,
        'name': _('menu_view_communication_objects'),
        'link': '/communication_objects/',
    },
    'menu_view_change_password': {
        'priority': 100,
        'name': _('menu_view_change_password'),
        'link': '/change_password/',
    },
}
