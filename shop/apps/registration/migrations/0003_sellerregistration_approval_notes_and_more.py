# Generated by Django 4.2.16 on 2024-10-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_sellerregistration_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerregistration',
            name='approval_notes',
            field=models.TextField(blank=True, null=True, verbose_name='Approval/Rejection Reasons'),
        ),
        migrations.AddField(
            model_name='sellerregistration',
            name='approval_status',
            field=models.CharField(db_index=True, default='P', max_length=2, verbose_name='Approval Status'),
        ),
    ]
