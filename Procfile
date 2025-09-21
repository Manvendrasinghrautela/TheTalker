web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn blog_project.wsgi --log-file - --bind 0.0.0.0:$PORT --workers 2 --timeout 120

