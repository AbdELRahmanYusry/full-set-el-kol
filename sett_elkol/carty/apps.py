from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class CartyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sett_elkol.carty'
    verbose_name = _("carty")
    
