# Указываем базовый образ
FROM python:3.13-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /habit_tracker

# Установка системных зависимостей
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root

# Копируем остальные файлы проекта в контейнер
COPY . .

# Создаем директорию для медиафайлов
RUN mkdir -p /habit_tracker/staticfiles && chmod -R 755 /habit_tracker/staticfiles

# Собираем статику и запускаем gunicorn
CMD sh -c "poetry run python manage.py collectstatic --noinput && poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000"