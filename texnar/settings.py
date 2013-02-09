DEBUG = 1
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Vlad Mekh', 'komduv@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'texnar',                     
        'USER': 'root',                      
        'PASSWORD': '123456',                
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''


STATIC_URL = '/home/vlad/workspace/chat/bin/texnar/static'


STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'bv-1ul#4oj$25o_*o7qon)*1z)vag3a#5fc%n0#po94%r^65m2'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'texnar.urls'

WSGI_APPLICATION = 'texnar.wsgi.application'
import os,sys
    
TEMPLATE_DIRS = (
     # os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
     '/home/vlad/workspace/chat/bin/texnar/templates/',
) 
"""
VK auth
"""
VK_APP_ID = '3378606'
VK_API_SECRET = 'NedWHFt49EHvYgTDMIeq'
"""
Google auth
"""
GOOGLE_OAUTH2_CLIENT_ID = '612934706766.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'JP8FFQsuPrGQ73zND-9ERdGG'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.vkontakte.VKontakteOAuth2Backend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'chat',
    'social_auth',
    'accounts',
    'django_socketio',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
