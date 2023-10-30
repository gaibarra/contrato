from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ALLOWED_HOSTS = [".herokuapp.com"]
ALLOWED_HOSTS = ['0.0.0.0','212.1.214.223','contratosmodelo.link','127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'd7p6erb1fvqq0v',
#        'HOST': 'ec2-44-207-133-100.compute-1.amazonaws.com',
#        'USER': 'igeypucwdvfkvl',
#        'PASSWORD': '0ce2682f24f296e645956e80e0c564cee0f52662c9be84c987d9b8f457ad5d7b',
#        'PORT': 5432
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'contrato',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': '6Vlgpcr/zaira',
        'PORT': 5432
    }
}


#import dj_database_url
#from decouple import config

#DATABASES = {
#    'default': dj_database_url.config(
#        default=config('DATABASE_URL')
#    )

#}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)