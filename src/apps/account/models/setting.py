from django.db import models
from django.contrib.auth.models import User


class Setting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_enable_notification = models.BooleanField(default=True)

    class Meta:
        db_table = 'auth_setting'
        app_label = 'account'

    def __str__(self):
        return f'{self.user.username} Setting'

    def save(self, *args, **kwargs):
        super(Setting, self).save(*args, **kwargs)