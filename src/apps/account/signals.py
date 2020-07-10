from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from apps.account.models import Profile, Setting


# This is receiver for: profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('create_user_profile')
        print(instance)
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# This is receiver for: Setting
@receiver(post_save, sender=User)
def create_user_setting(sender, instance, created, **kwargs):
    if created:
        print('create_user_setting')
        Setting.objects.create(user=instance)
        print('create_user_setting: done')


@receiver(post_save, sender=User)
def save_user_setting(sender, instance, **kwargs):
    instance.setting.save()
