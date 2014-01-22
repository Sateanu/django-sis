# probably not the best invocation
# celery usage is archaic but somehow works (for the gradebook), even without amqp
# SFTPStorage sucks https://bitbucket.org/david/django-storages/issue/135/sftpstoragesave-falls-on-heroku-with
web: mkdir /app/.ssh; touch /app/.ssh/known_hosts; gunicorn ecwsp.wsgi & python manage.py celerybeat & python manage.py celeryd
