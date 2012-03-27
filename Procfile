web: newrelic-admin run-program python skel/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3 --max-requests 1000 --settings=skel.settings.prod
scheduler: python skel/manage.py celeryd -B -E --maxtasksperchild=1000 --settings=skel.settings.prod
worker: python skel/manage.py celeryd -E --maxtasksperchild=1000 --settings=skel.settings.prod
