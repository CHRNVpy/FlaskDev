# Используйте официальный образ Python
FROM python:3.11-alpine

# Установите зависимости
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Скопируйте исходники приложения
COPY .. .

# Укажите порт для Flask-приложения
EXPOSE 8080

# Запустите ваше Flask-приложение
CMD ["python", "app.py"]