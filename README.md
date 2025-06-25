# FastApi

🚀 Учебный проект на FastAPI

## Описание

FastApi — это учебный проект для освоения FastAPI, SQLAlchemy и Pydantic. Реализованы CRUD-операции для пользователей и новостей, работа с базой данных SQLite, а также примеры REST API.

---

## Структура проекта

```
FastApiLearning/
├── src/
│   ├── api/           # Роутеры FastAPI
│   ├── database/      # Работа с БД и менеджеры
│   ├── models/        # SQLAlchemy модели
│   ├── schemas/       # Pydantic схемы
│   ├── main.py        # Создание FastAPI-приложения
│   ├── run.py         # Точка входа (запуск uvicorn)
│   └── news.db        # SQLite база данных
└── README.md
```

---

## Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/IlyaVlasov2007/FastApi.git
   cd FastApi
   ```
2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # или
   source venv/bin/activate  # Linux/Mac
   ```
3. **Установите зависимости:**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```
4. **Запустите сервер:**
   ```bash
   python src/run.py
   ```

---

## Документация API

После запуска перейдите на:
- Swagger UI: [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)
- ReDoc: [http://127.0.0.1:5000/redoc](http://127.0.0.1:5000/redoc)

---

## Примеры запросов

### Создать пользователя
```http
POST /user/
{
  "login": "user1",
  "password_hash": "hash",
  "role": 1
}
```

### Получить всех пользователей
```http
GET /user/
```

### Создать новость
```http
POST /article/
{
  "title": "Новость",
  "description": "Текст...",
  "author_id": 1
}
```

---

## Для разработки

- Все настройки БД — в `src/database/config.py`
- Модели — в `src/models/models.py`
- Схемы — в `src/schemas/`
- Роутеры — в `src/api/`

---