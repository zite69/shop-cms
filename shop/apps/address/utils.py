from .models import Country
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

def get_default_country():
    try:
        return Country.objects.get(iso_3166_1_a2="IN")
    except Country.DoesNotExist:
        raise ImproperlyConfigured(_("Please run python manage.py oscar_populate_countries --no-shipping before using this function"))