"""
ASGI config for offer_yangu project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'offer_yangu.settings')

application = get_asgi_application()
application = WhiteNoise(application,root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'))
