#!/bin/bash
# Create writable directories
mkdir -p /tmp/media
chmod 777 /tmp
chmod 777 /tmp/media

# Apply database migrations
python manage.py migrate

# Create superuser (remove in production)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell