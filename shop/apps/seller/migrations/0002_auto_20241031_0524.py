from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.text import slugify

def load_data(apps, schema_editor):
    #Seller = Seller
    from shop.apps.seller.models import Seller
    name = settings.ZITE69_MAIN_SELLER
    user_id = settings.ZITE69_MAIN_USER_ID
    User = get_user_model()
    user = User.objects.get(id = user_id)
    Seller.objects.create(
        name = name,
        handle = slugify(name),
        user = user
    )


class Migration(migrations.Migration):
    dependencies = [
        ('seller', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_data)
    ]