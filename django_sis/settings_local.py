ALLOWED_HOSTS = ['*']
#DEBUG = False
#LOGGING = {}
INSTALLED_APPS = (
    #'debug_toolbar',
    'ecwsp.benchmarks',
    'ecwsp.benchmark_grade',
    'ecwsp.work_study',
    'storages',
)

DEFAULT_FILE_STORAGE = 'storages.backends.sftpstorage.SFTPStorage'
SFTP_STORAGE_HOST = 'daphne.cristoreyny.org'
SFTP_STORAGE_ROOT = '/var/www/heroku_storage/'
SFTP_STORAGE_PARAMS = {
    'username': 'OMG NO WAY!',
    'password': 'SERIOUSLY!',
}
MEDIA_URL = 'http://daphne.cristoreyny.org:12345/heroku_storage/'

import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
