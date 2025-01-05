#setting for offline

# import dj_database_url
from pathlib import Path
import os
from decouple import config
import dj_database_url
from rest_framework.authentication import TokenAuthentication

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_task',
    'app_accounts',
    'app_query',
    'api',
    
    'app_manytomany',
    

    # 'app_todo',
    'app_todo.apps.AppTodoConfig' ,

    # pip install pillow
    #pip install crispy-bootstrap5
    "crispy_forms",
    "crispy_bootstrap5",
    #pip install django-formtools
    "formtools",
    #pip install djangorestframework
    #pip install markdown  
    # pip install django-filter
    'rest_framework',
    'rest_framework.authtoken',

    # third party app
    # pip install django-rest-auth
    'dj_rest_auth',


    # pip install 'dj-rest-auth[with_social]'
    

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    #  python -m pip install django-debug-toolbar
    #  "django.contrib.staticfiles",
    "debug_toolbar",     
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'django_maris.urls'
INTERNAL_IPS = [
    
    "127.0.0.1",

]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [
          os.path.join(BASE_DIR,"templates")
                 ],
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

WSGI_APPLICATION = 'django_maris.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     config('DB_NAME'),
        'USER':     config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
    },    
}





# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#crispy form
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = BASE_DIR/'static'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR,'assets'),
)


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA FILES CONFIG
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'

SITE_ID = 1
# '''email setting  '''
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =   config('EMAIL_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL=config('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND =config('EMAIL_BACKEND') 

# ACCOUNT_EMAIL_REQUIRED=config('ACCOUNT_EMAIL_REQUIRED') 
# ACCOUNT_AUTHENTICATION_METHOD =config('ACCOUNT_AUTHENTICATION_METHOD') 
# ACCOUNT_EMAIL_VERIFICATION= config('ACCOUNT_EMAIL_VERIFICATION')



from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# AUTH_USER_MODEL='account.Account'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
       [
       'rest_framework.authentication.TokenAuthentication',
    ],
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser'
    ]
}