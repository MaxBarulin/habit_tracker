# Трекер привычек

## Описание
Проект представляет собой веб-приложение для отслеживания привычек.
Используется стек: Django + DRF + Celery + Redis + PostgreSQL.

---

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:MaxBarulin/habit_tracker.git
   cd habit_tracker
   ```

2. Установите зависимости (если хотите запускать локально):
   ```bash
   pip install poetry
   poetry install
   ```

3. Создайте `.env` файл с переменными окружения:
   ```bash
   cp .env.example .env
   ```
   Заполните его своими данными.

4. (Опционально) Если вы используете Docker:
   ```bash
   docker-compose build
   docker-compose up
   ```

---

## Архитектура проекта

### Сервисы:
- **habit_tracker** — основное Django-приложение (API и фронтенд)
- **postgres** — PostgreSQL для хранения данных
- **redis** — брокер сообщений для Celery
- **celery** — обработчик асинхронных задач
- **celery-beat** — планировщик периодических задач

---

## Использование

Запустите приложение через Docker Compose:
```bash
docker-compose up
```

После запуска:
- Админка: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## Проверка работоспособности сервисов

После запуска проверьте, что все контейнеры работают:
```bash
docker-compose ps
```

Результат должен быть примерно таким:
```
NAME                             COMMAND                  STATUS              PORTS
habit_tracker-habit_tracker-1    "poetry run gunicorn …"  Up                  0.0.0.0:8000->8000/tcp
habit_tracker-postgres-1         "docker-entrypoint.s…"     Up                  5432/tcp
habit_tracker-redis-1            "docker-entrypoint.s…"     Up                  6379/tcp
habit_tracker-celery-1           "poetry run celery -A …" Up
habit_tracker-celery-beat-1      "poetry run celery -A …" Up
```

### Проверка каждого сервиса:

#### 1. **PostgreSQL**
Проверьте, что БД доступна:
```bash
docker-compose exec postgres psql -U postgres -c "SELECT version();"
```

#### 2. **Redis**
Проверьте, что Redis работает:
```bash
docker-compose exec redis redis-cli ping
```
> Ответ должен быть: `PONG`

#### 3. **Django (web)**  
Откройте [http://localhost:8000](http://localhost:8000), должно открыться приложение или API.

#### 4. **Celery worker**
Логи:
```bash
docker-compose logs celery
```
Убедитесь, что нет ошибок подключения к Redis и БД.

#### 5. **Celery Beat**
Логи:
```bash
docker-compose logs celery-beat
```
Убедитесь, что планировщик запущен корректно.

---

## Тестирование

Запустите тесты внутри контейнера:
```bash
docker-compose run habit_tracker poetry run python manage.py test
```

---

## Деплой на сервер

1. Подключитесь к серверу по SSH:
   ```bash
   ssh user@your_server_ip
   ```

2. Склонируйте репозиторий:
   ```bash
   git clone git@github.com:MaxBarulin/habit_tracker.git
   cd habit_tracker
   ```

3. Установите Docker и Docker Compose:
   ```bash
   sudo apt update && sudo apt install docker.io docker-compose -y
   ```

4. Запустите проект:
   ```bash
   docker-compose up -d
   ```

5. Примените миграции:
   ```bash
   docker-compose run habit_tracker poetry run python manage.py migrate
   ```

6. (Опционально) Создайте суперпользователя:
   ```bash
   docker-compose run habit_tracker poetry run python manage.py createsuperuser
   ```

---

## Переменные окружения

Создайте `.env` файл на основе примера:
```bash
cp .env.example .env
```

Пример содержимого `.env`:
```env
# Настройки базы данных
NAME=habit_db
USER=postgres
PASSWORD=postgres
PORT=5432

# Email (опционально)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password
SECRET_KEY=your_secret_key_here
DEBUG=True
```

---

## Полезные команды

| Назначение | Команда |
|-----------|---------|
| Посмотреть логи | `docker-compose logs -f` |
| Остановить контейнеры | `docker-compose down` |
| Применить миграции | `docker-compose run habit_tracker poetry run python manage.py migrate` |
| Собрать статику | `docker-compose run habit_tracker poetry run python manage.py collectstatic --noinput` |
| Запустить shell в контейнере | `docker-compose run habit_tracker bash` |

---

## CI/CD

Проект настроен на автоматический деплой через GitHub Actions:
- При пуше в `main` происходит:
  - Сборка и тестирование
  - Запуск миграций
  - Перезапуск контейнеров на сервере

---

## Автор

Максим Барулин  
Telegram: @max_barulin  
Email: maxbarulin@gmail.com