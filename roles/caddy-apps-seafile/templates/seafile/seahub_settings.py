# -*- coding: utf-8 -*-
SECRET_KEY = "b'*z^c(c16#xy$bx-f3yl61$y@0rh$o$-74xx+_-oj+&=+$-oc0)'"
FILE_SERVER_ROOT = "https://{{ app_subdomain }}.{{ domain_name }}/seafhttp"
SERVICE_URL = "https://{{ app_subdomain }}.{{ domain_name }}/"
CSRF_TRUSTED_ORIGINS= ["https://{{ app_subdomain }}.{{ domain_name }}"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': '{{ mariadb_seafile_user_passwd }}',
        'HOST': 'seafile-db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

##### Redis
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://default:{{ redis_password }}@seafile-redis:6379",
#     },
#      'locmem': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     },
# }

##### Memcached
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'seafile-memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

COMPRESS_CACHE_BACKEND = 'locmem'
TIME_ZONE = 'Etc/UTC'

### Email
EMAIL_USE_TLS = False
EMAIL_HOST = '{{ email_smtp_host }}' 
EMAIL_HOST_USER = '{{ email_user }}'
EMAIL_HOST_PASSWORD = '{{ email_password }}'
EMAIL_PORT = '{{ email_smtp_port }}'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = True # for TLS with 465, see [https://manual.seafile.com/config/sending_email/]


### SSO 
ENABLE_OAUTH = True
OAUTH_CLIENT_ID = "seafile"
OAUTH_CREATE_UNKNOWN_USER = True
OAUTH_ACTIVATE_USER_AFTER_CREATION = True
OAUTH_ENABLE_INSECURE_TRANSPORT = False
OAUTH_CLIENT_SECRET = "{{ seafile_secret }}" 
OAUTH_REDIRECT_URL = 'https://{{ app_subdomain}}.{{domain_name }}/oauth/callback/'

OAUTH_PROVIDER   = '{{ keycloak_auth_domain }}'
OAUTH_PROVIDER_DOMAIN   = '{{ keycloak_auth_domain }}'
OAUTH_AUTHORIZATION_URL = '{{ keycloak_auth_url}}/realms/{{keycloak_realm }}/protocol/openid-connect/auth'
OAUTH_TOKEN_URL         = '{{ keycloak_auth_url}}/realms/{{keycloak_realm }}/protocol/openid-connect/token'
OAUTH_USER_INFO_URL     = '{{ keycloak_auth_url}}/realms/{{keycloak_realm }}/protocol/openid-connect/userinfo'
OAUTH_SCOPE = ["openid", "profile", "email"]
OAUTH_ATTRIBUTE_MAP = {
    "id":    (False, "not used"), # Seafile <v11 compatibility
    "uid":    (False, "not used"), # Seafile v11.0 +
    "name":  (False, "full name"), 
    "email": (True, "email"),
}



{% if onlyoffice_enabled == 'true' %}
# Enable OnlyOffice
ENABLE_ONLYOFFICE = True
VERIFY_ONLYOFFICE_CERTIFICATE = True
ONLYOFFICE_APIJS_URL = 'https://office.{{ domain_name }}/web-apps/apps/api/documents/api.js'
ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
ONLYOFFICE_EDIT_FILE_EXTENSION = ('docx', 'pptx', 'xlsx')

# Enable force save to let user can save file when he/she press the save button on OnlyOffice file edit page.
ONLYOFFICE_FORCE_SAVE = True
ONLYOFFICE_JWT_SECRET = '{{ onlyoffice_jwt }}'
{% endif %}


