"""
ASGI config for web_t_project project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t_project.settings')

application = get_asgi_application() 