# Generated by Django 4.2.16 on 2024-10-31 19:29

from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model
import string
import random

def generate_password(length=10):
    #Generate a random password of specified length after remvoing confusing characters
    #like l and 1, O and 0
    characters = string.ascii_letters.replace('l', '').replace('O', '') + string.digits.replace('0', '').replace('1', '')
    return "".join(random.choice(characters) for i in range(length))

def create_system_users(apps, schema_editor):
    #User = apps.get_model('user', 'User')
    User = get_user_model()
    sys_pass = generate_password()
    print(f"user: system , password: {sys_pass}")
    User.objects.create_superuser(username=settings.ZITE69_MAIN_USERNAME, password=sys_pass, first_name='System', last_name='User') 
    with open(settings.BASE_DIR / "local/password.txt", "w") as f:
        f.write(sys_pass)

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_phone'),
    ]

    operations = [
        migrations.RunPython(create_system_users)
    ]
