from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthUser(AbstractUser):
    password = models.CharField(max_length=128, verbose_name='Пароль')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='Останній вхід')
    is_superuser = models.BooleanField(verbose_name='Суперюзер')
    username = models.CharField(unique=True, max_length=150, verbose_name='Ім\'я користувача')
    first_name = models.CharField(max_length=150, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=150, verbose_name='Призвище')
    email = models.CharField(unique=True, max_length=254, verbose_name='Email адреса')
    is_staff = models.BooleanField(verbose_name='Персонал')
    is_active = models.BooleanField(verbose_name='Активний')
    date_joined = models.DateTimeField(verbose_name='Дата приєднання')
    user_role = models.ForeignKey('UserRole', models.DO_NOTHING, db_column='user_role', verbose_name='Роль')

    USERNAME_FIELD = 'username'

    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name = 'Аутентифікований користувач'
        verbose_name_plural = 'Аутентифіковані користувачі'

class UserRole(models.Model):
    role_name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'user_role'

class Phone(models.Model):
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user', verbose_name='id користувача')
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер телефону')

    class Meta:
        verbose_name = 'Номер телефону'
        verbose_name_plural = 'Номери телефонів'
        ordering = ['id']
        managed = False
        db_table = 'phone'