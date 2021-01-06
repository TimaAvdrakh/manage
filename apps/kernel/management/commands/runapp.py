from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run worker'

    def handle(self, *args, **options):
        print('RunAPP')
