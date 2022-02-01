from django.apps import AppConfig


class BaseConfigs(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
