"""
WSGI config for Blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf.urls.static import static
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')

application = get_wsgi_application()