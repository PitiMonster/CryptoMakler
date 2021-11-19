import sys
from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True
        # you must import your modules here
        # to avoid AppRegistryNotReady exception
        print('siema siema')
        global APIClient
        from .models import FakeAPI
        APIClient = FakeAPI()
        # startup code here
