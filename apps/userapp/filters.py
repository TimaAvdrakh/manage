import django_filters

from apps.userapp.models import MainUser


class MainUserFilter(django_filters.FilterSet):
    class Meta:
        model = MainUser
        fields = ['organization', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()
