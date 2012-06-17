web: newrelic-admin run-program gunicorn -c gunicorn.py.ini wsgi:application
scheduler: python manage.py celeryd -B -E --maxtasksperchild=1000
worker: python manage.py celeryd -E --maxtasksperchild=1000
