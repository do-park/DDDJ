"""
WSGI config for web_pjt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_pjt.settings.production')

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_pjt.settings')

application = get_wsgi_application()
