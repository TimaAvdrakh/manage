from django.contrib.auth.models import Permission, Group

from apps.system import MENU_ITEMS


def menu_context(request):
    context_data = dict()
    user = request.user

    if not request.user.is_authenticated:
        return context_data
    groups = Group.objects.filter(user=user).all()
    permissions = set(Permission.objects.filter(user=user))

    for group in groups:
        permissions.update(set(group.permissions.all()))

    items = []
    for perm in permissions:
        if 'menu_view' in perm.codename:
            item = MENU_ITEMS.get(perm.codename)
            if item:
                items.append(item)

    items = sorted(items, key=lambda k: k.get('priority'))

    context_data['menu_items'] = items
    return context_data
