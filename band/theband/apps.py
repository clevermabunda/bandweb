from django.apps import AppConfig

class ThebandConfig(AppConfig):
    """
    Configuration class for the 'theband' application.

    Attributes:
        default_auto_field (str): The default field type for auto-generated primary keys.
        name (str): The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theband'
