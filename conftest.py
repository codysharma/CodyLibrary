import pytest
from django.conf import settings

@pytest.fixture(scope="session")
def django_db_setup():
    """Setup the database for testing."""
    from django.conf import settings
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
    settings.DATABASES['default']['TEST'] = {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3'
    }