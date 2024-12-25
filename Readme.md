# Python Web Application

Це простий веб-додаток на Python, який дозволяє користувачам відправляти та читати повідомлення.


## Вимоги

- Python 3.9+
- Docker (опціонально)

## Запуск

### Без Docker

1. Запустіть головний скрипт:
python main.py

2. Відкрийте браузер і перейдіть за адресою `http://localhost:3000`

### З Docker

1. Створіть Docker образ:
docker build -t python-web-app .

2. Запустіть Docker контейнер:
docker run -p 3000:3000 -v ./docker_data:/app/storage python-web-app

3. Відкрийте браузер і перейдіть за адресою `http://localhost:3000`

## Структура проекту

- `main.py`: Головний скрипт додатку
- `index.html`: Головна сторінка
- `message.html`: Сторінка для відправки повідомлень
- `read_template.html`: Шаблон для відображення повідомлень
- `error.html`: Сторінка помилки 404
- `style.css`: CSS стилі
- `Dockerfile`: Конфігурація для створення Docker образу
- [storage/data.json](cci:7://file:///Users/dimkabalakin/Neoversity/Tier_2/FullStack_Web_Development_with_Python/goit-pythonweb-hw-03/storage/data.json:0:0-0:0): Файл для зберігання повідомлень

## Використання

- Перейдіть на головну сторінку для перегляду інформації про курси Python
- Використовуйте сторінку "Send message" для відправки нового повідомлення
- Перегляньте всі повідомлення на сторінці "Read messages"

