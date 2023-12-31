from .common import *

from pathlib import Path
from dotenv import load_dotenv
import os
import socket
load_dotenv()
import logging.config
from django.utils.log import DEFAULT_LOGGING
from django.core.management.color import supports_color

DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
PRODUCTION = 0

# Application definition
RUN_SERVER_PORT = 8000

SUPER_USER_NAME = os.environ.get("SUPER_USER_NAME")
SUPER_USER_PASSWORD = os.environ.get("SUPER_USER_PASSWORD")
SUPER_USER_FIRST_NAME = os.environ.get("SUPER_USER_FIRST_NAME")
SUPER_USER_LAST_NAME = os.environ.get("SUPER_USER_LAST_NAME")

# --------------------------------------------------------------
# EMAIL SETTINGS
# --------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)
EMAIL_HOST_USER = os.environ.get("DONOT_REPLY_EMAIL")
DISPLAY_NAME = os.environ.get("EMAIL_DISPLAY_NAME")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
# --------------------------------------------------------------
# END EMAIL SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# DATABASE SETTINGS
# --------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
# --------------------------------------------------------------
# END DATABASE SETTINGS
# --------------------------------------------------------------


# --------------------------------------------------------------
# STATIC FILE SETTINGS
# --------------------------------------------------------------
STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'static'),
        os.path.join(BASE_DIR,'media'),
        ]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR,'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR,'media_cdn')

# --------------------------------------------------------------
# END STATIC FILE SETTINGS
# --------------------------------------------------------------


# --------------------------------------------------------------
# HEDERA SETTINGS
# --------------------------------------------------------------
HEDERA_OPERATOR_ID =  os.environ.get('OPERATOR_ID')
HEDERA_OPERATOR_KEY = os.environ.get('OPERATOR_KEY')
HEDERA_OPERATOR_PRIVATE_KEY = os.environ.get('OPERATOR_PRIVATE_KEY')
HEDERA_ENV = os.environ.get('HEDERA_ENV')
# --------------------------------------------------------------
# END HEDERA SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# LOGGING SETTINGS
# --------------------------------------------------------------
LOGFILEPATH = os.environ.get('LOGFILEPATH')
CELERYLOGFILEPATH = os.environ.get('CELERYLOGFILEPATH')
LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG' if DEBUG else 'INFO').upper()
CELERY_TASKS_LOGGER_NAME = "celery_tasks"

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # see more parameters at https://docs.python.org/3/library/logging.html#logging.LogRecord
            'format': '[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },

        'hashgraphhub.json.formatter': {
            'class': 'utils.logger.hashgraphhubJsonFormatter'
        },

        'colorlog': {
            'class': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },

        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{asctime}] {message}',
            'datefmt': "%Y-%m-%d %H:%M:%S",
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'colorlog.StreamHandler' if supports_color() else 'logging.StreamHandler',
            'formatter': 'colorlog' if supports_color() else 'console',
            # 'filters': ['require_debug_true']
        },

        'rotating_file': {
            'class': 'utils.logger.BetterRotatingFileHandler',
            'formatter': 'hashgraphhub.json.formatter',
            # 'filters': ['require_debug_true'],
            'filename': LOGFILEPATH,
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
        'celery_rotating_file': {
            'class': 'utils.logger.BetterRotatingFileHandler',
            'formatter': 'hashgraphhub.json.formatter',
            # 'filters': ['require_debug_true'],
            'filename': CELERYLOGFILEPATH,
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },

        'django.server': DEFAULT_LOGGING['handlers']['django.server'],

    },
    'loggers': {
        # "root" logger which serves as a catch-all for any logs that are sent from any Python module
        '': {
            'level': 'ERROR',
            'handlers': ['console', 'rotating_file'],
        },

        'django': {
            'handlers': ['console', 'rotating_file'],
            'level': 'ERROR',
        },

        'django.request': {
            'handlers': ['console', 'rotating_file'],
            'level': LOGLEVEL,
            'propagate': False,
        },

        # DB queries
        'django.db.backends': {
            'handlers': ['console', 'rotating_file'],
            'level': 'ERROR',
            'propagate': False,
        },

        # Logging From Your Application
        'hashgraphhub': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        'users': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        'external_apis': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },
        CELERY_TASKS_LOGGER_NAME: {
            'level': LOGLEVEL,
            'handlers': ['console', 'celery_rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        # Django-internals logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],

    },
})


# --------------------------------------------------------------
# END LOGGING SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# CORS SETTINGS
# --------------------------------------------------------------
CORS_ORIGIN_WHITELIST = [
    'http://localhost:4173',
    'http://app:4173'
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4173",
    "http://127.0.0.1:4173",
]

CORS_ALLOW_CREDENTIALS = True
# --------------------------------------------------------------
# END CORS SETTINGS
# --------------------------------------------------------------
