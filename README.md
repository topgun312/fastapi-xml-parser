# Тестовое задание Python Backend Developer Middle

## Задача: XML Parser & AI Analyzer Service

### Описание:
- Разработать микросервис, который будет ежедневно получать XML-файл с данными о продажах, обрабатывать его и генерировать аналитический отчет с помощью LLM.

### Технические требования:
#### Основной функционал:
1. Создать сервис на FastAPI/Django
2. Реализовать планировщик задач (например, используя Celery)
3. Сервис должен:
- Получать XML файл по URL: ``
- Парсить данные о продажах (товары, количество, цены)
- Сохранять данные в PostgreSQL
- Формировать промпт для LLM с анализом продаж
- Сохранять ответ LLM в базу данных

#### Пример промпта для LLM:
Проанализируй данные о продажах за {date}:
1. Общая выручка: {total_revenue}
2. Топ-3 товара по продажам: {top_products}
3. Распределение по категориям: {categories}

Составь краткий аналитический отчет с выводами и рекомендациями.

### Технический стек:
- Python 3.10+
- FastAPI/Django
- PostgreSQL
- Celery
- Docker
- OpenAI API/Claude AP
- Poetry/pip для управления зависимостями

### Требования к реализации:
1. Код должен быть размещен на GitHub
2. Наличие Docker-compose для запуска сервиса
3. README.md с инструкцией по запуску
4. Unit-тесты для основных компонентов
5. Логирование операций
6. Обработка ошибок
7. API документация (Swagger/OpenAPI)

### Дополнительные плюсы:
- Использование асинхронного программирования
- Реализация кэширования
- Мониторинг работы сервиса
- CI/CD pipeline
- Конфигурация через переменные окружения

### Запуск проекта на локальном сервере
1. Клонировать репозиторий
- git clone https://github.com/topgun312/fastapi-xml-parser.git
2. Cоздать и активировать виртуальное окружение, установить зависимости:
- (venv) $ cd backend
- poetry install
3. Создать файл .env и записать следующие аргументы

- DB_NAME=postgres - название БД
- DB_HOST=localhost - название сервера
- DB_PORT=5432 - порт для подключения к БД
- DB_USER=postgres - логин для подключения к БД
- DB_PASS=postrges - пароль для подключения к БД

- MODE=DEV - режим разработки

- REDIS_HOST=redis - название сервиса redis
- REDIS_PORT=6379 - порт для подключения к redis


4. Создаем миграции (в проекте уже будут созданы миграции с соответсвующими настройками для БД):
   -  alembic revision --autogenerate -m "Add table"

5. Применяем миграции:
   - alembic upgrade head

6. Запускаем приложение:
   - uvicorn main:app --reload


### Запуск проекта в docker-контейнере
1. Клонировать репозиторий
- git clone https://github.com/topgun312/fastapi-xml-parser.git

2. Создать файл .env-non-dev для продакшена и записать к аргументам из файла .env следующие аргументы
- POSTGRES_DB=postgres - название БД
- POSTGRES_USER=postgres - логин для подключения к БД
- POSTGRES_PASSWORD=postgres - пароль для подключения к БД

3. Собрать образ docker-контейнера
- docker-compose build --no-cache

4. Запустить docker-контейнер
- docker-compose up

### Для запуска тестов 
1. Создать файл .test.env и записать следующие аргументы
- DB_NAME=test_postgres - название тестовой БД
- DB_HOST=localhost - название сервера
- DB_PORT=5432 - порт для подключения к БД
- DB_USER=postgres - логин для подключения к БД
- DB_PASS=postrges - пароль для подключения к БД

- MODE=TEST - режим тестирования

2. Запуск тестов 
- pytest -vv tests/