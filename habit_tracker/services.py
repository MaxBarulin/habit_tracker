import requests

from config.settings import TELEGRAM_URL, API_TOKEN_TELEGRAM


class SendMessageTelegram:
    """Отправляет пользователю напоминание о привычке в телеграм, с помощью бота"""

    @staticmethod
    def send_message(chat_id, message):
        params = {
            'text': message,
            'chat_id': chat_id
        }
        requests.get(f"{TELEGRAM_URL}{API_TOKEN_TELEGRAM}/sendMessage", params=params)
