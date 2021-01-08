from django.core.management.base import BaseCommand

from apps.kernel.services import creational


class Command(BaseCommand):
    help = 'Run worker'

    def handle(self, *args, **options):
        print('RunAPP')
        wc = creational.WorkerCreator()
        wc.up()
