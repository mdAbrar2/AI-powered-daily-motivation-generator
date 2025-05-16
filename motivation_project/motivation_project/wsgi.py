"""
WSGI config for motivation_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/motivation project'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'motivation_project.settings'

# Activate your virtualenv if you have one
activate_this = '/home/yourusername/motivation project/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()