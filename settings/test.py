"""
Test-specific Django settings.
"""

# Inherit from base settings
from .base import *     # pylint:disable=W0614,W0401

TEST_APPS = (
    'openassessment',
    'openassessment.assessment',
    'openassessment.groups',
    'openassessment.workflow',
    'openassessment.xblock',
)

# Configure nose
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=' + ",".join(TEST_APPS),
    '--cover-branches',
    '--cover-erase',
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# Install test-specific Django apps
INSTALLED_APPS += ('django_nose',)


# We run Celery in "always eager" mode in the test suite,
# which executes tasks synchronously instead of using the task queue.
CELERY_ALWAYS_EAGER = True


# Silence cache key warnings
# https://docs.djangoproject.com/en/1.4/topics/cache/#cache-key-warnings
import warnings
from django.core.cache import CacheKeyWarning
warnings.simplefilter("ignore", CacheKeyWarning)
