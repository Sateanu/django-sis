# probably not the best invocation
# celery usage is archaic
web: gunicorn ecwsp.wsgi & python manage.py celerybeat & python manage.py celeryd
