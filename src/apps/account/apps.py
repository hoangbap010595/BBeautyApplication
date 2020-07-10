from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'apps.account'
    verbose_name = 'account manage'

    def ready(self):
        import apps.account.signals
