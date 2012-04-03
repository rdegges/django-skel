web: newrelic-admin run-program python {{ project_name }}/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3 --max-requests 1000 --settings={{ project_name }}.settings.prod
scheduler: python {{ project_name }}/manage.py celeryd -B -E --maxtasksperchild=1000 --settings={{ project_name }}.settings.prod
worker: python {{ project_name }}/manage.py celeryd -E --maxtasksperchild=1000 --settings={{ project_name }}.settings.prod
