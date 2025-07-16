from rest_framework.exceptions import ValidationError


class RewardValidator:
    """
    Валидатор проверяет, что нельзя выбирать одновременно вознаграждение и приятную привычку,
    также приятная привычка не может иметь вознаграждения или связанной привычки.
    """

    def __init__(self, reward, related_habit, sign_pleasant_habit):
        self.reward = reward
        self.related_habit = related_habit
        self.sign_pleasant_habit = sign_pleasant_habit

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        related_habit = dict(value).get(self.related_habit)
        sign_pleasant_habit = dict(value).get(self.sign_pleasant_habit)

        if sign_pleasant_habit is True:
            if reward is not None or related_habit is not None:
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")

        if reward is related_habit:
            raise ValidationError("Нужно выбрать вознаграждение (reward) или приятную привычку (related_habit).")
        elif reward is not None and related_habit is not None:
            raise ValidationError("Нельзя одновременно выбрать вознаграждение и приятную привычку.")


class TimeToCompleteValidator:
    """Валидатор проверяет время выполнения привычки (не более 120 секунд)."""

    def __init__(self, time_to_complete):
        self.time_to_complete = time_to_complete

    def __call__(self, value):
        time_to_complete = dict(value).get(self.time_to_complete)
        if time_to_complete and int(time_to_complete) > 120:
            raise ValidationError("Время выполнения привычки не может быть больше 120 секунд.")


class RelatedHabitValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __init__(self, related_habit):
        self.related_habit = related_habit

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        if related_habit and related_habit.sign_pleasant_habit is False:
            raise ValidationError("Связанная привычка, может быть только с признаком приятной привычки.")
