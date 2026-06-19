# apps/leave/apps.py
from django.apps import AppConfig

class LeaveConfig(AppConfig):  # Changed from AppConfig to LeaveConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.leave'

    def ready(self):
        import apps.leave.signals
