import os
import sys
import dj_database_url

if os.path.isfile('env.py'):
    import env

from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent



# ======================
# Security
# ======================

# Use environment variable in production
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'replace-me-with-a-secure-key'
)

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.herokuapp.com',
]


# ======================
# Applications
# ======================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cloudinary storage app (placed immediately after staticfiles)
    'cloudinary_storage',

    # Project apps
    'blog',
    'about',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_summernote',
    'crispy_forms',
    'crispy_bootstrap5',
    'cloudinary',
    # 'dj3_cloudinary_storage',  # not required; using cloudinary_storage
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Sites framework and Allauth redirects
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# ======================
# Middleware
# ======================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ======================
# URLs / WSGI
# ======================

ROOT_URLCONF = 'codestar.urls'

WSGI_APPLICATION = 'codestar.wsgi.application'


# ======================
# Templates
# ======================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# ======================
# Database
# Use DATABASE_URL when provided (e.g., production), otherwise fall back to SQLite for local dev.
# ======================

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

if 'test' in sys.argv:
    # Use SQLite for the test runner to avoid touching production DB
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    # Use simple staticfiles storage during tests to avoid Manifest lookup errors
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]
# ======================
# Password validation
# ======================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Allauth settings
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Crispy forms (Bootstrap5)
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# ======================
# Internationalization
# ======================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ======================
# Static files
# ======================

STATIC_URL = '/static/'

# Additional static files directory for project-level static assets
# Additional static files directory for project-level static assets
STATICFILES_DIRS = [
    os.path.join(str(BASE_DIR), 'static'),
]

# Directory where `collectstatic` will collect static files for production
STATIC_ROOT = os.path.join(str(BASE_DIR), 'staticfiles')

# Use WhiteNoise storage backend to serve compressed static files in production
if 'test' in sys.argv:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ======================
# Default PK field
# Path for project-level templates directory
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Cloudinary storage
# If you set the environment variable `CLOUDINARY_URL`, use Cloudinary for media storage.
# Example (DO NOT commit your keys):
# CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
if os.environ.get('CLOUDINARY_URL'):
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    # Local media fallback for development
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')