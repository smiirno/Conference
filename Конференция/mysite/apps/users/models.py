from django.db import models


class User(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    login = models.CharField('Логин', max_length=20)
    password = models.CharField('Пароль', max_length=20)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
