from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse, reverse_lazy


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

    USERNAME_FIELD = 'username'

    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name = 'Аутентифікований користувач'
        verbose_name_plural = 'Аутентифіковані користувачі'

    def __str__(self):
        return self.username

class Reviews(models.Model):
    author = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='author', verbose_name='Автор')
    content = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Зміст')
    timestamp_review = models.DateTimeField(auto_now_add=True, verbose_name='Позначка часу')

    class Meta:
        managed = False
        db_table = 'reviews'
        ordering = ['id']
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'

    def get_absolute_url(self):
        return reverse_lazy('detail_review', kwargs={'pk': self.pk})