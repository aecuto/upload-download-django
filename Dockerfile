FROM python:3.8
RUN apt update
RUN useradd -u 1000 -d /app -M -s /bin/false app \
	&& pip install poetry gunicorn
ENV POETRY_VIRTUALENVS_CREATE=false
ENV DEBUG=false

COPY . /app/
WORKDIR /app/
RUN poetry install --no-dev --no-interaction \
	&& python manage.py collectstatic --no-input

RUN mkdir files && chown 1000:1000 files
RUN mkdir database && chown 1000:1000 database

USER 1000

RUN python manage.py migrate

CMD ["gunicorn", "--access-logfile", "-", "--error-logfile", "-", "-b", "0.0.0.0:8080", "-t", "300", "--threads", "16", "send.wsgi:application"]