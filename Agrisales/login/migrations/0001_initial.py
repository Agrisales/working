# Generated by Django 3.2.4 on 2021-06-11 11:10

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('phone_number', models.TextField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Phone number')),
                ('user_name', models.CharField(max_length=64, verbose_name='User name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Last login')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
