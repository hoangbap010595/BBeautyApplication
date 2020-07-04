"""
ASGI config for bbeauty project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from bbeauty.conf import app_settings

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', app_settings.SETTINGS_MODULE_PATH)

application = get_asgi_application()
