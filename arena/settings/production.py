from arena.settings.common import *
import os
DEBUG = False
ALLOWED_HOSTS = []
SECRET_KEY = os.environ('DJANGO_SECRET_KEY')

# Remember to set after setting up production database.
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ('DJANGO_DB_NAME'),
            'USER': os.environ('DJANGO_DB_USERNAME'),
            'PASSWORD': os.environ('DJANGO_DB_PW'),
            'HOST': 'localhost',
            'PORT': '',
    }
}