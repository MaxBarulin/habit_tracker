from django.contrib import admin

from habit_tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "action",
        "user",
        "SignPleasantHabit",
        "RelatedHabit",
        "Periodicity",
        "SignPublic",
    )
    list_filter = (
        "id",
        "user",
        "SignPleasantHabit",
        "RelatedHabit",
        "Periodicity",
        "SignPublic",
    )
    search_fields = (
        "id",
        "user",
        "SignPleasantHabit",
        "RelatedHabit",
        "Periodicity",
        "SignPublic",
    )