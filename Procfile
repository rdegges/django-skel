web: newrelic-admin run-program python /manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
scheduler: python manage.py celeryd -B -E --maxtasksperchild=1000
worker: python manage.py celeryd -E --maxtasksperchild=1000
