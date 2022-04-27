import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 定义字节包加入python的环境变量
sys.path.insert(0,os.path.join(BASE_DIR, 'blog'))

SECRET_KEY = 'm@z7t#8u7u+o$hwb$@g!6i6&!n(^@wgdv9t^+gbo(w0w7+d4k*'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'account',
    'article',
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

ROOT_URLCONF = 'laoqi_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'laoqi_django.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'laoqi_django',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

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

# 语言设置
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 静态内容
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# MEDIA_URL = 'static/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

#登录后重定向到http://127.0.0.1/blog/页面
LOGIN_REDIRECT_URL = '/home/'
# LOGIN_REDIRECT_URL = '/blog/'

# 防止没有登录修改密码，跳转到django默认页面，报错,这样可以直接调到登录界面，省去了后续的麻烦
LOGIN_URL = '/account/login/'

# 设置密码找回邮箱
EMAIL_HOST = 'smtp.qq.com'
EMAIL_HOST_USER = "572534940@qq.com"
EMAIL_HOST_PASSWORD = "1973702576wj"
EMAIL_PORT = 25
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "572534940@qq.com"
# 将邮件直接显示在控制台
# EMAIL_BACKED='django.core.mail.backends.console.EmailBackend'

# 配置redis
REDIS_HOST = '192.168.10.70'
REDIS_PORT = 6379
REDIS_DB = 15