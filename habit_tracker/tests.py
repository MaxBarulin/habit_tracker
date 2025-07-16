from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitTrackerTestCase(APITestCase):
    """Класс тестирования модели привычки."""

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            tg_chat_id=123,
            password=123
        )

        self.habit = Habit.objects.create(
            user=self.user,
            location="Дом",
            time="12:30:00",
            action="Посидеть",
            sign_pleasant_habit=False,
            time_to_complete=60,
            reward="посидеть",
            sign_public=False
        )

        self.data = {
            "user": 1,
            "location": "Дом",
            "time": "12:30:00",
            "action": "Посидеть",
            "sign_pleasant_habit": False,
            "time_to_complete": 60,
            "reward": "посидеть",
            "sign_public": False
        }

        self.client.force_authenticate(user=self.user)
        self.url = '/habit/'

    def test_create_habit(self):
        """Тестирование создания привычки"""

        response = self.client.post(self.url, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {'id': 2, 'location': 'Дом', 'time': '12:30:00', 'action': 'Посидеть',
             'sign_pleasant_habit': False, 'periodicity': 1, 'reward': 'посидеть', 'time_to_complete': 60,
             'sign_public': False, 'related_habit': None}
        )

    def test_retrieve_all_habit(self):
        """Проверяем вывод списка всех привычек."""

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_publish_habit_list(self):
        """Проверяем просмотр одной привычки"""
        url = reverse("habit_tracker:publish_habit_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
