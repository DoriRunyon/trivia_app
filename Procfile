web: gunicorn trivia_app.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=trivia_app -B --loglevel=info
