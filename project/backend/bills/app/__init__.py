from django.apps import AppConfig


class BillsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.bills.app'
    verbose_name = 'bills'
    label = 'bills'

    def ready(self):
        import backend.bills.app.signals