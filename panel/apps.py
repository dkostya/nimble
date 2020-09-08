from django.apps import AppConfig


class PanelConfig(AppConfig):
    name = 'panel'

    def ready(self):

        from workers import updater
        updater.start()

