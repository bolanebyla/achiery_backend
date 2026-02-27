# Achiery
Сервис для прокачки личных навыков и выполнения целей: 
- ачивки - прокачка навыков 
- квесты - разовые задачи
- вызовы - периодические задачи / привычки

## 🛠 Технологии

- **Python 3.13+**
- **[Django](https://www.djangoproject.com/)**
- **[Django rest framework](https://www.django-rest-framework.org/)**
- **[Gunicorn](https://gunicorn.org/)** - WSGI-сервер
- **[UV](https://github.com/astral-sh/uv)** - менеджер пакетов Python 


## 🚀 Запуск проекта

Каталог `src/` является корневым для python модулей проекта,
например в IDE можно его пометить как sources_root
(в случае запуска из консоли, нужно определить `PYTHONPATH` и сослать на этот
каталог)

TODO

### 🐳 Docker

TODO

## Запуск компонентов окружения (docker-compose)
TODO

## 🧪 Тестирование

Запуск тестов

```bash
pytest
```

## Openapi документация

- Файл документации доступен по адресу http://127.0.0.1:8000/swagger/?format=openapi
- Swagger доступен по адресу http://127.0.0.1:8000/swagger

## 🔍 Линтеры

В проекте используется [Ruff](https://github.com/astral-sh/ruff)

### Настройка линтера

Конфигурация линтера находится в файле `pyproject.toml` в секции `[tool.ruff]`

### Запуск линтера
```bash
ruff check .
```

Автоматическое исправление проблем
```bash
ruff check --fix .
```

## 🔒 Pre-commit

В проекте настроен pre-commit для автоматической проверки кода перед коммитом. 
Настройки pre-commit находятся в файле `.pre-commit-config.yaml`.

### Установка pre-commit

```bash
pre-commit install
```

После этого pre-commit будет автоматически запускаться перед каждым коммитом.
