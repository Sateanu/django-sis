ALLOWED_HOSTS = ['*']
#DEBUG = False
#LOGGING = {}
INSTALLED_APPS = (
    #'debug_toolbar',
    'ecwsp.benchmarks',
    'ecwsp.benchmark_grade',
    'ecwsp.work_study',
)

import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
