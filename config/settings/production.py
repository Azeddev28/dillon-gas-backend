from config.settings.base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}