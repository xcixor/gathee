release: python src/core/manage.py migrate
web: gunicorn --chdir ./src/core/ core.wsgi