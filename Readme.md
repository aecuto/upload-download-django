poetry run python manage.py makemigrations 
poetry run python manage.py migrate


poetry run python manage.py runserver 

poetry run gunicorn send.wsgi:application

poetry run python manage.py remove_expired_files



docker-compose up -d
localhost:8080