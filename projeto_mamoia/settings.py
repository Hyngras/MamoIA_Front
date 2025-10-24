"""
Django settings for projeto_mamoia project.
Gerenciado via variáveis de ambiente (.env) com django-environ.
"""

from pathlib import Path
import environ
import os

# Caminhos base
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------
# Variáveis de ambiente (.env)
# ---------------------------------------------
env = environ.Env(
    DEBUG=(bool, False),
)
# Lê o arquivo .env na raiz do projeto (mesmo nível do manage.py)
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Segurança e debug
DEBUG = env("DEBUG", default=False)
SECRET_KEY = env("SECRET_KEY", default="change-me")  # não deixar assim em produção
ALLOWED_HOSTS = [h.strip() for h in env("ALLOWED_HOSTS", default="").split(",") if h.strip()]

# Redirecionamentos pós-login/logout (mantive os seus)
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"

# ---------------------------------------------
# Apps
# ---------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api_rest",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <--- Adicione aqui
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "projeto_mamoia.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Se tiver uma pasta templates/ na raiz, ela já é considerada aqui
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "api_rest.context_processors.static_version",
            ],
        },
    },
]

WSGI_APPLICATION = "projeto_mamoia.wsgi.application"

# ---------------------------------------------
# Banco de dados (MySQL via .env ou fallback SQLite)
# ---------------------------------------------
if env("DB_ENGINE", default="sqlite").lower() == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
            "HOST": env("DB_HOST", default="127.0.0.1"),
            "PORT": env("DB_PORT", default="3306"),
            "OPTIONS": {
                "charset": "utf8mb4",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ---------------------------------------------
# Validação de senha (padrão Django)
# ---------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------------
# Localização
# ---------------------------------------------
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Recife"  # ajustado para seu fuso
USE_I18N = True
USE_TZ = True  # Django armazena em UTC e apresenta no fuso acima

# ---------------------------------------------
# Arquivos estáticos e mídia
# ---------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"   # coleta para produção (collectstatic)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Versão de static para cache busting em templates (ex: ?v={{ STATIC_VERSION }})
STATIC_VERSION = os.getenv("STATIC_VERSION", "1")

# ---------------------------------------------
# Email via .env (sem credenciais no código)
# ---------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_PORT = int(env("EMAIL_PORT", default=587))
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or "no-reply@example.com"

# ---------------------------------------------
# Usuário customizado (mantive o seu)
# ---------------------------------------------
AUTH_USER_MODEL = "api_rest.User"

# (Opcional) Backends — inclua um backend por e-mail se você tiver implementado
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # "api_rest.backends.EmailBackend",  # descomente se existir
]

# ---------------------------------------------
# Chave primária padrão
# ---------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
