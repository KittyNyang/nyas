"""
Django settings for scriptslide project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qjvif0w)2)q(_v9g+s1%fyc5@&!jjcmh8*3vl$hc2_4f1#oh0w'

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
    'django.contrib.sites',
    'script',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'drf_yasg',
    'corsheaders'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'scriptslide.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'scriptslide.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

#USE_I18N = True

#USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


REST_FRAMEWORK = {
    '''
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    '''
    
    
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=256),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=256),
}

'''
JWT_SECRET_KEY: JWT의 비밀키(Secret Key)로 어떤걸 사용할지 작성합니다. 여기에서는 장고(django)와 같은 비밀키를 사용하였지만 사용할 때는 다른 키를 사용하시길 권장합니다.
JWT_ALGORITHM: JWT 암호화에 사용되는 알고리즘을 지정합니다.
JWT_ALLOW_REFRESH: JWT 토큰을 갱신할 수 있게 할지 여부를 결정합니다.
JWT_EXPIRATION_DELTA: JWT 토큰의 유효 기간을 설정합니다.
JWT_REFRESH_EXPIRATION_DELTA: JWT 토큰 갱신의 유효기간 입니다.


REST_USE_JWT = True     #login시 JWT 이용

SESSION_COOKIE_AGE = 12096000          #20주동안 세션 저장
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  #브라우저가 닫혀도 세션 저장
SESSION_SAVE_EVERY_REQUEST = True       #세션이 날라올 떄 마다 갱신
'''


TOKEN_EXPIRED_AFTER_SECONDS = 60*60*24*30*12 #1년


ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True  #우선은 USERNAME으로만 로그인
SITE_ID = 1             #  rest auth 사용 시 DB 위치 명시localhost에서


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

