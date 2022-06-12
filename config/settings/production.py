from config.settings.base import *

import dj_database_url


prod_db = dj_database_url.config(conn_max_age=500)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# CHANGE THIS ACCORDINLY TO THE DOMAIN SELECTED
ALLOWED_HOSTS = ['dillon-gas-app.herokuapp.com']

DATABASES = {
    'default': prod_db
}
