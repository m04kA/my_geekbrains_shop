import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "pzegz3ade%pvc00#@7bxcz9mt8tv(^l!5a9iks0t_@)ra#&om$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "mainapp",
    "authnapp",
    "basketapp",
    "adminapp",
    "social_django",
    "ordersapp",
]

# Django Crispy Forms
#   Official docs | https://django-crispy-forms.readthedocs.io/en/latest/
#   Tutorial (ru) | https://django.fun/tutorials/django-i-formy-bootstrap-4/
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Auth model
AUTH_USER_MODEL = "authnapp.ShopUser"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "best_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mainapp.context_processors.basket",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "best_shop.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "best_shop",
        "USER": "postgres"
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]
else:
    # Set simple password for debug
    AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Media files
MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Set login path:
#   https://docs.djangoproject.com/en/2.2/ref/settings/#login-url
LOGIN_URL = "authnapp:login"

DOMAIN_NAME = "http://localhost:8000"

# Read about sending email:
#   https://docs.djangoproject.com/en/2.2/topics/email/

# Full list of email settings:
#   https://docs.djangoproject.com/en/2.2/ref/settings/#email
EMAIL_HOST = "localhost"
EMAIL_PORT = "25"

EMAIL_USE_SSL = False
# If server support TLS:
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = "django@best_shop.local"
# EMAIL_HOST_PASSWORD = "best_shop"
# For debugging: python -m smtpd -n -c DebuggingServer localhost:25
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None

# Email as files
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "tmp/email-messages/"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "social_core.backends.vk.VKOAuth2",
)

# SOCIAL_AUTH_AUTHENTICATION_BACKENDS = ("social_core.backends.vk.VKOAuth2",)
SOCIAL_AUTH_URL_NAMESPACE = "social"

# You can save settings in file, but not in GIT!
# SOCIAL_AUTH_VK_OAUTH2_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# SOCIAL_AUTH_VK_OAUTH2_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Load settings from file
with open(".secrets/vk.json", "r") as f:
    VK = json.load(f)

SOCIAL_AUTH_VK_OAUTH2_KEY = VK["SOCIAL_AUTH_VK_OAUTH2_APPID"]
SOCIAL_AUTH_VK_OAUTH2_SECRET = VK["SOCIAL_AUTH_VK_OAUTH2_KEY"]

LOGIN_ERROR_URL = "/"

SOCIAL_AUTH_VK_OAUTH2_IGNORE_DEFAULT_SCOPE = True
# Full list of scope here:
#     https://vk.com/dev/permissions
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ["email"]

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.create_user",
    "authnapp.pipeline.save_user_profile",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)