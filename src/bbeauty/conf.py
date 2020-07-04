
class DefaultSettings:
    def _setting(self, name, default=None):
        from django.conf import settings
        return getattr(settings, name, default)

    @property
    def SETTINGS_MODULE_PATH(self):
        """
        Settings module path
            1. development
            2. staging
            3. production
        """
        return "bbeauty.settings.development"

    @property
    def BBEAUTY_PAGGING_LENGTH(self):
        """
        Pagging one page
        """
        return self._setting('BBEAUTY_PAGGING_LENGTH', 25)

    def __getattr__(self, key):
        if not key.startswith('BBEAUTY'):
            key = 'BBEAUTY_' + key
        return self.__getattribute__(key)


app_settings = DefaultSettings()
