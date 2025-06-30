"""
Django settings for cafemenu project.
Optimized for Vercel + Neon PostgreSQL
"""

from pathlib import Path
import os
import dj_database_url
from decouple import config
from dotenv import load_dotenv

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent


# Security
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-dev-key')  # Use env var in production
DEBUG = False  
ALLOWED_HOSTS = [
    '.vercel.app',
    'digital-cafe-menu.onrender.com',
    '.now.sh',
    '127.0.0.1',
    'localhost',
    'ed-burgers.onrender.com',
    'everyday-burger.et',
    '188.245.213.109'  # VPS IP address
]
# CSRF_TRUSTED_ORIGINS is used to whitelist domains that are allowed to make requests to the server.
CSRF_TRUSTED_ORIGINS = [
    "http://188.245.213.109",
    "https://188.245.213.109",
]

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'menu',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
]

ROOT_URLCONF = 'cafemenu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'menu/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cafemenu.wsgi.application'

# Database Configuration (Neon PostgreSQL)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        engine='django.db.backends.postgresql',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Media files (Vercel compatible)
MEDIA_URL = '/media/'
#MEDIA_ROOT = ''
load_dotenv(os.path.join(BASE_DIR, '.env'))
# Cloudinary configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),  # Matches Render's key
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
    'SECURE': True,  # Enforce HTTPS
    'EXCLUDE_DELETE_ORPHANED_MEDIA': True,  # Prevent accidental deletions
    'QUALITY': 'auto:good'  # Optimize images
}

# File storage settings
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Add to settings.py to confirm config on startup
try:
    import cloudinary
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET')
    )
    print("✅ Cloudinary configured successfully")
except Exception as e:
    print(f"❌ Cloudinary error: {str(e)}")
# Static files (Whitenoise optimized)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Custom admin styling
ADMIN_SITE_HEADER_COLOR = "#c93835"
ADMIN_SITE_BUTTON_COLOR = "#e67e22"

# Security headers (production only)
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False