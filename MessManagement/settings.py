import os
import ldap
from django_auth_ldap.config import LDAPSearch

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'DrB1C7nxwUnuMrEWjZzFMArieyWEIOFUqlssMAgdW5n2WASHog4fZt0DlgLV97Dr6qMCULc2VO3sT1zL4eWMGorOYWW3ZNwUIN2zBpQNSXKlcdOV7okFEqhk8Iqmw8tb'

# CLIENT_ID = 'pOMAobpIHqaiBEaa3LthpDlmJyYUHujUJ9FchCOa'
CLIENT_ID='EweyNhXjTyzHejczRPAFEJIDkIDnqQgW8leK8Y3A'
CLIENT_SECRET = 'DrB1C7nxwUnuMrEWjZzFMArieyWEIOFUqlssMAgdW5n2WASHog4fZt0DlgLV97Dr6qMCULc2VO3sT1zL4eWMGorOYWW3ZNwUIN2zBpQNSXKlcdOV7okFEqhk8Iqmw8tb'
SSO_TOKEN_URL = 'https://gymkhana.iitb.ac.in/sso/oauth/token/'
OAUTH_BASE_URL = 'https://gymkhana.iitb.ac.in/sso/'
AUTHORISE_URL = 'oauth/authorize/'
LOGIN_URL = 'oauth/'
TOKEN_URL = 'oauth/token/'
TOKEN_REVOKE_URL = 'oauth/revoke_token/'
USER_API_URL = 'user/api/user/'
USER_SEND_MAIL_API_URL = 'user/api/user/send_mail/'
REDIRECT_URI_1 = 'http://localhost:8800/mess/callback'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'guestBook.User'

#adding LDAP authentication backend 
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
] 

#Baseline Configuration
AUTH_LDAP_SERVER_URI = 'ldap://ldap.iitb.ac.in'
AUTH_LDAP_BIND_DN = ''
AUTH_LDAP_BIND_PASSWORD = ''
AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=People,dc=iitb,dc=ac,dc=in',
    ldap.SCOPE_SUBTREE,
    '(uid=%(user)s)')

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name':'givenName',
    'last_name':'sn',
    'email':'mail',
}

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

AUTH_LDAP_PROFILE_ATTR_MAP = {
    'roll_number' : 'employeeNumber',
    'user_type' : 'employeeType',
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guestBook',

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

ROOT_URLCONF = 'MessManagement.urls'

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

WSGI_APPLICATION = 'MessManagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
