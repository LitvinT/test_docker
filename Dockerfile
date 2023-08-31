# Используйте официальный образ Python
FROM python:3.11

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файлов
COPY app.py /app/app.py
COPY templates /app/templates

# Установка зависимостей
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Запуск приложения
CMD ["python", "app.py"]
