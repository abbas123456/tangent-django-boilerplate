import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_code }}_stage', # Or path to database file if using sqlite3.
        'USER': '{{ project_code}}_app', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
            'init_command': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;',
        }
    },
}

EMAIL_SUBJECT_PREFIX = '[{{ project_code }}][Stage] '
LOG_ROOT = os.path.join(os.path.dirname(__file__), '../../../logs/stage')
