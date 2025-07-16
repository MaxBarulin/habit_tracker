from celery import shared_task
from django.utils import timezone

from habit_tracker.models import Habit
from habit_tracker.services import SendMessageTelegram


@shared_task
def send_habit_for_user():
    """Функция отправки привычек для пользователей в телеграм"""

    date_now = timezone.now().date()
    all_a_habit = Habit.objects.filter(sign_pleasant_habit=False)
    all_habit_now = [habit for habit in all_a_habit if habit.time.date() == date_now]

    for habit in all_habit_now:
        message = f"Я буду {habit.action} в {habit.time.time()} в {habit.location}"
        chat_id = habit.user.tg_chat_id
        SendMessageTelegram.send_message(chat_id=chat_id, message=message)  # в сервисном модуле
