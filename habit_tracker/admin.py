from django.contrib import admin

from habit_tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "action",
        "user",
        "sign_pleasant_habit",
        "reward",
        "related_habit",
        "periodicity",
        "sign_public",
    )
    list_filter = (
        "id",
        "user",
        "sign_pleasant_habit",
        "related_habit",
        "periodicity",
        "sign_public",
    )
    search_fields = (
        "id",
        "user",
        "sign_pleasant_habit",
        "related_habit",
        "periodicity",
        "sign_public",
    )
