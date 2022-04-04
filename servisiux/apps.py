from django.apps import AppConfig


class ServisiuxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servisiux'

    def ready(self):
        from .signals import create_profile, save_profile
        