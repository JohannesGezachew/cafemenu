#!/bin/bash
# Create writable directories
mkdir -p /tmp/media
chmod 777 /tmp
chmod 777 /tmp/media

# Apply database migrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput