import django_filters

from apps.kernel import models


class MainUserFilter(django_filters.FilterSet):
    class Meta:
        model = models.Task
        fields = ['organization', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()
