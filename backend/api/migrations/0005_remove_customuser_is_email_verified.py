# Generated by Django 5.1.3 on 2025-01-01 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_email_verified',
        ),
    ]
