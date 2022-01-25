#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn --access-logfile - --error-logfile - -b 0.0.0.0:8080 -t 300 --threads 16 send.wsgi:application