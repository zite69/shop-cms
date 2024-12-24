# Generated by Django 4.2.17 on 2024-12-16 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='seller_admins', to=settings.AUTH_USER_MODEL, verbose_name='Shop Admin'),
        ),
        migrations.AddField(
            model_name='seller',
            name='ceo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='seller_ceos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='seller', to=settings.AUTH_USER_MODEL, verbose_name='Seller User'),
        ),
        migrations.AddConstraint(
            model_name='seller',
            constraint=models.UniqueConstraint(condition=models.Q(models.Q(('gstin', ''), _negated=True), ('gstin__isnull', False)), fields=('gstin',), name='unique_gstin_in_seller_ifnotnull'),
        ),
        migrations.AddConstraint(
            model_name='seller',
            constraint=models.UniqueConstraint(condition=models.Q(models.Q(('pan', ''), _negated=True), ('pan__isnull', False)), fields=('pan',), name='unique_pan_in_seller_ifnotnull'),
        ),
    ]