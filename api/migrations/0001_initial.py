# Generated by Django 4.1.7 on 2023-04-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('avatar_url', models.ImageField(upload_to='avatars/')),
                ('description', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('occupation', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('residential_addresses', models.ManyToManyField(to='api.address')),
            ],
        ),
    ]