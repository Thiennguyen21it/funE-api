# Generated by Django 4.1.7 on 2023-04-07 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_residential_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='residential_address',
        ),
    ]
