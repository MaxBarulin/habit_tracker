# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager  # Импортируем менеджер

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    - Аутентификация по email.
    - Поле username остается в модели, но может быть необязательным.
    """

    # --- ПОЛЕ USERNAME НЕ УДАЛЕНО ---
    # Оно остается в модели. Мы просто убираем требование уникальности по умолчанию
    # и делаем его необязательным на уровне Django, если это нужно.
    # Если вы хотите, чтобы никнеймы все же были уникальными, оставьте unique=True.
    username = models.CharField(
        max_length=255,
        verbose_name='Имя пользователя (никнейм)',
        unique=True,  # Оставим уникальным, но это можно изменить
        **NULLABLE  # Позволяет создавать пользователя без username через API/формы
    )

    # --- ПОЛЕ EMAIL СТАНОВИТСЯ ГЛАВНЫМ ---
    email = models.EmailField(
        _('email address'),
        unique=True  # Email теперь должен быть уникальным
    )

    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name='Телеграм чат-id',
        unique=True,
        **NULLABLE
    )

    # --- НАСТРОЙКИ АУТЕНТИФИКАЦИИ ---
    # Указываем Django, что для входа используется поле email
    USERNAME_FIELD = 'email'

    # Поля, которые нужно будет обязательно заполнить при создании суперпользователя в консоли
    REQUIRED_FIELDS = ['username']

    # Подключаем кастомный менеджер
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
