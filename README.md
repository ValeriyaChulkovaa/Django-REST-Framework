# Django DRF Homework 33

## 🚀 Особенности

- **Уведомления по email** при обновлении курсов
- **Блокировка неактивных пользователей** (30+ дней без входа)
- Периодические задачи с **Celery Beat**
- Документация API (Swagger/ReDoc)
- Тесты с покрытием 91%

## ⚙️ Требования

- Python 3.10+
- Redis (брокер для Celery)
- Poetry (менеджер зависимостей)
- Docker

## 🛠 Установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/ValeriyaChulkovaa/Django-REST-Framework.git
```

### 2. Установка Redis
- **Ubuntu/Debian**:
  ```bash
  sudo apt install redis-server
  ```
- **MacOS** (с Homebrew):
  ```bash
  brew install redis
  ```

### 3. Установка зависимостей
```bash
pip install poetry
poetry install
```

## 🏃 Запуск проекта
В терминале/командной строке вводим:
```bash
docker compose up --build
```

## 🧪 Тестирование
Запуск тестов с отчетом о покрытии:
```bash
pytest --cov --cov-report=html
```
Откройте `htmlcov/index.html` для просмотра деталей покрытия.

## 📖 Документация API
Доступна после запуска сервера:
- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


## 📧 Функционал уведомлений
- Отправка email при:
  - Добавлении нового урока в курс
  - Обновлении курса/урока (если прошло >4 часов с последнего обновления)
- Периодическая проверка активности пользователей


## 👨💻 Автор
Ваше имя  
[GitHub](https://github.com/Sweerx)