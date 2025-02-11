FROM python:3.11

ENV PYTHONUNBUFFERED=1

ENV MYSQL_ROOT_PASSWORD example_password

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

