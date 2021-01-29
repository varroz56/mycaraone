from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
    # importing signals to config
    def ready(self):
        import profiles.signals
