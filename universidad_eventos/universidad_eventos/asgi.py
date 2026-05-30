"""
ASGI config for universidad_eventos project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad_eventos.settings')

application = get_asgi_application()
