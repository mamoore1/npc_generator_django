"""
WSGI config for npc_generator_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'npc_generator_website.settings')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
