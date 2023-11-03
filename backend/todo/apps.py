from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name = "todo"
