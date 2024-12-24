# Generated by Django 4.2.17 on 2024-12-18 16:32

from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_auto_20181115_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')], max_length=64, verbose_name='Title')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last name')),
                ('line1', models.CharField(max_length=255, verbose_name='First line of address')),
                ('line2', models.CharField(blank=True, max_length=255, verbose_name='Second line of address')),
                ('line3', models.CharField(blank=True, max_length=255, verbose_name='Third line of address')),
                ('line4', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State/County')),
                ('postcode', oscar.models.fields.UppercaseCharField(blank=True, max_length=64, verbose_name='Post/Zip-code')),
                ('search_text', models.TextField(editable=False, verbose_name='Search text - used only for searching addresses')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Organization Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Organization Address',
                'verbose_name_plural': 'Organization Addresses',
                'abstract': False,
            },
        ),
    ]
