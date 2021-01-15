#!/bin/sh

python wait_for_postgres.py

python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"