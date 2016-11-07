"""
WSGI config for application project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
import os
import sys


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

application = get_wsgi_application()
root_path = os.path.abspath(os.path.split(__file__)[0])
