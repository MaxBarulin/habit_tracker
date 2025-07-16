from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "username",
        "tg_chat_id",
    )
    list_filter = (
        "username",
        "tg_chat_id",
    )
    search_fields = ("id", "username", "tg_chat_id",)
