# Generated by Django 4.1.7 on 2023-04-08 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_user_residential_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(default=1234, max_length=10),
            preserve_default=False,
        ),
    ]
