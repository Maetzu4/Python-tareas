"""
WSGI config for universidad_eventos project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad_eventos.settings')

application = get_wsgi_application()
