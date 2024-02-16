#!/bin/sh

python manage.py migrate --noinput || exit 1

export DJANGO_SUPERUSER_PASSWORD=root
export DJANGO_SUPERUSER_EMAIL=example@example.com
export DJANGO_SUPERUSER_USERNAME=admin

python manage.py seed
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

exec "$@"