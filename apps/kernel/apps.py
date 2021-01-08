from django.apps import AppConfig


class KernelConfig(AppConfig):
    name = 'apps.kernel'

    def ready(self):
        import apps.kernel.signals  # noqa
