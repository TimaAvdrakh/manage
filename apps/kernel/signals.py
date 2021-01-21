from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.kernel import models
from apps.kernel.services import creational


# @receiver(post_save, sender=models.CommunicationObject)
# def change_com_state(sender, instance, **kwargs):
#     wc = creational.WorkerCreator()
#     if instance.state:
#         wc.start_proc(instance.id)
#     else:
#         wc.kill_proc(instance.id)
