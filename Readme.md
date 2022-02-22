# Upload & Download file
 - user register/login/logout
 - upload file (auth)
 - download file (with link)
 - delete file (auth)
 - auto delete expire file every 2 minutes


## Setup
```sh
$ poetry install

```

## Develop
```sh

# for database
$ poetry run python manage.py makemigrations 
$ poetry run python manage.py migrate

# dev reload
$ poetry run python manage.py runserver 

# serve
$ poetry run gunicorn send.wsgi:application

# goin -> localhost:8000

# command remove the expire file
poetry run python manage.py remove_expired_files

```


## Docker
```sh
$ docker-compose up -d --build

# then exec migrate in container
$ python manage.py migrate

# goin -> localhost:8080
```


