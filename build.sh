#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations (if using SQLite or other DB)
python manage.py migrate

# Optional: Create superuser (remove in production)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell