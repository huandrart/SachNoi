"""
Django settings for websachnoi project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}



# SECRET_KEY = 'django-insecure-=fooya_i(jg4(xcq0-71!67%a=3q38inmnn(98o(*2uha*in5_'
SECRET_KEY = config('SECRET_KEY')




# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sachnoi',
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

ROOT_URLCONF = 'websachnoi.urls'

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

WSGI_APPLICATION = 'websachnoi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'defaultdb',  # Tên cơ sở dữ liệu của bạn
#         'USER': 'avnadmin',  # Tên người dùng MySQL
#         'PASSWORD': 'AVNS_Xo7hEecALufhRtngeQP',  # Mật khẩu MySQL
#         'HOST': 'mysql-4c55101-minhtrivo2005gg-b6de.c.aivencloud.com',  # Địa chỉ máy chủ MySQL (localhost nếu đang chạy trên máy tính cục bộ)
#         'PORT': '26715',  # Cổng của MySQL (mặc định là 3306)
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # hoặc mysql, sqlite3
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# settings.py

# Cấu hình email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Sử dụng SMTP để gửi email
EMAIL_HOST = 'smtp.gmail.com'  # Máy chủ SMTP của Gmail
EMAIL_PORT = 587  # Cổng SMTP, thường là 587 cho TLS
EMAIL_USE_TLS = True  # Sử dụng mã hóa TLS (bảo mật)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Địa chỉ email của bạn
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Mật khẩu email của bạn
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Địa chỉ email gửi đi (thường là EMAIL_HOST_USER)


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'