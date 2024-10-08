"""
Django settings for biblioteca project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e=%igdchzh@#iy81%t76m^pi**!xd9m@5!cpm0@nf&533m6^37'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livro',
    'usuarios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'biblioteca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'livro.context_processors.usuario_autenticado',
            ],
        },
    },
]

WSGI_APPLICATION = 'biblioteca.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "biblioteca",
#         "USER": "",
#         "PASSWORD": "",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }
env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env('ENVIRONMENT', default='development')

if ENVIRONMENT == 'production':
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL'))
     }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "biblioteca",
            "USER": "biblioteca",
            "PASSWORD": "biblioteca",
            "HOST": "127.0.0.1",
            "PORT": "5432",
            }   
        }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Expira a sessão quando o navegador é fechado
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Tempo de expiração da sessão em segundos (ex: 30 minutos)
SESSION_COOKIE_AGE = 3000  # 50 minutos

# Expira sessão após 5 minutos de inatividade
SESSION_COOKIE_AGE = 600  # 10 minutos
SESSION_SAVE_EVERY_REQUEST = True

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Defina a URL para login e logout
# LOGIN_URL = '/auth/login/'
# LOGIN_REDIRECT_URL = 'home'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '7a0d-177-38-244-186.ngrok-free.app']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok-free.app']

# CSRF_TRUSTED_ORIGINS = ['https://1a6b-177-38-244-186.ngrok-free.app']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'biblioteca-gerenciamento.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://biblioteca-gerenciamento.up.railway.app']