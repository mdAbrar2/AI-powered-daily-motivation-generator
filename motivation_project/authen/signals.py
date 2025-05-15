from django.apps import AppConfig

class AuthenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authen'

    def ready(self):
        import authen.signals  # Import the signals to connect them