from rest_framework.serializers import ModelSerializer

from habit_tracker.models import Habit
from habit_tracker.validators import (RelatedHabitValidator, RewardValidator,
                                      TimeToCompleteValidator)


class HabitSerializer(ModelSerializer):
    """Класс сериализатор привычки."""

    class Meta:
        model = Habit
        exclude = ('user',)
        validators = [
            RewardValidator(
                reward='reward',
                related_habit='related_habit',
                sign_pleasant_habit='sign_pleasant_habit'
            ),
            TimeToCompleteValidator(time_to_complete='time_to_complete'),
            RelatedHabitValidator(related_habit='related_habit')
        ]


class PublishHabitSerializer(ModelSerializer):
    """Класс сериализатор пользователя."""

    class Meta:
        model = Habit
        fields = "__all__"
