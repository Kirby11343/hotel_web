# Generated by Django 4.0.4 on 2022-05-14 10:08

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Останній вхід')),
                ('is_superuser', models.BooleanField(verbose_name='Суперюзер')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name="Ім'я користувача")),
                ('first_name', models.CharField(max_length=150, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=150, verbose_name='Призвище')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='Email адреса')),
                ('is_staff', models.BooleanField(verbose_name='Персонал')),
                ('is_active', models.BooleanField(verbose_name='Активний')),
                ('date_joined', models.DateTimeField(verbose_name='Дата приєднання')),
                ('role', models.CharField(blank=True, max_length=100, null=True, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Аутентифікований користувач',
                'verbose_name_plural': 'Аутентифіковані користувачі',
                'db_table': 'auth_user',
                'managed': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер телефону')),
            ],
            options={
                'verbose_name': 'Номер телефону',
                'verbose_name_plural': 'Номери телефонів',
                'db_table': 'phone',
                'ordering': ['id'],
                'managed': False,
            },
        ),
    ]
