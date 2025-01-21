from django.apps import AppConfig
# from sachnoi import signals

class SachnoiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sachnoi'
    def ready(self):
        import sachnoi.signals
