import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITE_ID = 1

PROJECT_APPS = (
    'sitetree',
)

INSTALLED_APPS = (
    'django',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'south',
) + PROJECT_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'tests.test_runner'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
SECRET_KEY = 'testkey'

if __name__ == "__main__":
    import sys, test_runner as settings
    from django.core.management import execute_manager
    if len(sys.argv) == 1:
        sys.argv += ['test'] + list(PROJECT_APPS)
    execute_manager(settings)
