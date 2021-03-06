import os
import sys


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

sys.path.append(
    os.path.join(os.path.dirname(BASE_DIR))
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = dict(
    default=dict(
        ENGINE='django.db.backends.sqlite3',
        NAME='example.db',
        USER='',
        PASSWORD='',
        HOST='',
        PORT='',
    )
)

INSTALLED_APPS = [
    # Project app
    'django_mptt_example',

    # Generic apps
    'mptt',
    'django_mptt_admin',

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

STATIC_URL = '/static/'
ROOT_URLCONF = 'example_project.urls'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# django jenkins settings
try:
    import django_jenkins
    INSTALLED_APPS.append('django_jenkins')
except ImportError:
    pass

PROJECT_APPS = ['django_mptt_admin', 'django_mptt_example']

JENKINS_TASKS = (
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
)