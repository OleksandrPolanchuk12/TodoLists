# Використовуємо офіційний образ Python 3.10
FROM python:3.10

# Встановлюємо змінну середовища для коректного логування
ENV PYTHONUNBUFFERED=1

ENV MYSQL_ROOT_PASSWORD example_password

# Встановлюємо робочий каталог
WORKDIR /app

# Копіюємо файл з залежностями перед усіма іншими файлами (щоб скористатися кешем Docker)
COPY requirements.txt .

# Оновлюємо pip і встановлюємо залежності
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копіюємо увесь код у контейнер
COPY . .

# Відкриваємо порт для веб-додатку
EXPOSE 8080

# Використовуємо Gunicorn для продакшн-сервера (замість вбудованого runserver)
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
