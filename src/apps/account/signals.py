from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from apps.account.models import Profile, Setting
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# This is receiver for: profile, Setting


@receiver(post_save, sender=User)
def create_user_profile_setting(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('created_user_profile')
        Setting.objects.create(user=instance)
        print('created_user_setting')

        if instance.email:
            try:
                body_html = render_to_string(
                    "account/bbeauty_welcome.html", {"user": instance}
                )
                email = EmailMessage(
                    subject='CHÀO MỪNG ĐẾN VỚI BBEAUTY',
                    body=body_html,
                    to=[instance.email]
                )
                email.content_subtype = 'html'
                email.send()
                print('send_mail_oke')
            except:
                print('send_mail_error')
                pass


@receiver(post_save, sender=User)
def save_user_profile_setting(sender, instance, **kwargs):
    instance.profile.save()
    instance.setting.save()
