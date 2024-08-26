# Общие настройки, которые используются во всех средах (разработка, тестирование, продакшн)

import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'main.urls'

INTERNAL_IPS = [
    '127.0.0.1',
]

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    os.getenv('MAIN_URL', 'http://'),
]

CSRF_COOKIE_DOMAIN = os.getenv('CSRF_COOKIE_DOMAIN', '.subdomain.com')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

TRACKING_ACTIVITY = None

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token YOUR_TOKEN': {
            'type': 'apikey',
            'in': 'header',
        },
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
}

DJANGO_SWAGGER = None

# Настройки документации drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'Pretty Pet',
    'DESCRIPTION': 'Pretty Pet test documentation',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}