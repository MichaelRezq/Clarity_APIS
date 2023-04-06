"""
Django settings for clarity project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mg6s*wfa&6i!2pnw6*@g73my09o(nfmr=&vjjp5k2(d#lk0+9y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',


    'rest_framework',
    'rest_framework.authtoken',

    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    

    
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github', # new

    'users',
    'jobs',
    'clarity',
    'posts',
    'comments',
    'problems',
    'replays',
    'community',
    # 'solutions',
    'chat',
    'ads',
    # 'solutions',
    'events',
    
]


AUTHENTICATION_BACKENDS = (
     # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # output emails to console for testing

# allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_VERIFICATION_SENT_REDIRECT_URL = 'http://localhost:3000/login'

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[MyApp] '
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True

# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'METHOD': 'oauth2',
#         'SCOPE': ['email'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'INIT_PARAMS': {'cookie': True},
#         'FIELDS': [
#             'id',
#             'email',
#             'name',
#             'first_name',
#             'last_name',
#             'verified',
#             'locale',
#             'timezone',
#             'link',
#             'gender',
#             'updated_time',
#         ],
#         'EXCHANGE_TOKEN': True,
#         'LOCALE_FUNC': lambda request: 'en_US',
#         'VERIFIED_EMAIL': False,
#         'VERSION': 'v12.0',
#     }
# }


# SOCIAL_AUTH_FACEBOOK_KEY = 'your-app-id'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'your-app-secret'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id, name, email, first_name, last_name'}


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online'
        },
                'OAUTH_PKCE_ENABLED': True,
        'APP': {
            'client_id': '528493647143-i8b2v3k4aoia0nf2vaqgm8pae1qan7mj.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}
# Client_ID = '528493647143-i8b2v3k4aoia0nf2vaqgm8pae1qan7mj.apps.googleusercontent.com'
# Client_secret = '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'
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = Client_ID
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = Client_secret
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['profile', 'email']
# SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
#     'access_type': 'offline'
# }
# SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://localhost:8000/accounts/google/login/callback/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    

]

ROOT_URLCONF = 'clarity.urls'

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




REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.IsAuthenticated'
    'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    ],
 }


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'clarity',
            'USER': 'michael',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': '5432',
        }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'clarity',
#         'USER': 'michael',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CORS_ALLOW_ALL_ORIGINS = True
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
#  for custmizing the allauth user

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.api.serializers.CustomRegisterSerializer',
}




AUTH_USER_MODEL = 'users.Custom'

import os

# Actual directory user files go to
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

# URL used to access the media
MEDIA_URL = '/media/'

# email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'michrezq@gmail.com'  # Replace with your email address
EMAIL_HOST_PASSWORD = 'jogqdvtzwmsrwrhw'  # Replace with your email password

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10  # Change to the desired number of attempts
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 3600  # Change to the desired number of seconds


WSGI_APPLICATION = 'clarity.wsgi.application'
ASGI_APPLICATION = 'clarity.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}