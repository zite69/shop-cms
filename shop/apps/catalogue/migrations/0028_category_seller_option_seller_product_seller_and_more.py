# Generated by Django 4.2.17 on 2024-12-24 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
        ('catalogue', '0027_attributeoption_code_attributeoptiongroup_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller'),
        ),
        migrations.AddField(
            model_name='option',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller'),
        ),
        migrations.AddField(
            model_name='productclass',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller'),
        ),
    ]
