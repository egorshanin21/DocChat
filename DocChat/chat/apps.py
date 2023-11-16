from django.apps import AppConfig

class ChatConfig(AppConfig):
    """
    Class defining the configuration for the "Chat" application.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Field for automatically selecting the type of primary key field.
    name = 'chat'  # Application name.

