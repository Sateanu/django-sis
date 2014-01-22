# probably not the best invocation
# celery usage is archaic but somehow works (for the gradebook), even without amqp
web: gunicorn ecwsp.wsgi & python manage.py celerybeat & python manage.py celeryd
