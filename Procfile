# web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn mysite.wsgi
release: python manage.py migrate