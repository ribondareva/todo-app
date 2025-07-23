# Flask TODO App with Priority

Простое веб-приложение для управления задачами с поддержкой приоритетов, созданное на Flask.

## Особенности

- Добавление задач с указанием приоритета (низкий, средний, высокий)
- Визуальное отображение приоритета (цветная полоса слева)
- Отметка выполненных задач (перечёркивание текста)
- Удаление задач
- Лёгкий и понятный интерфейс

## Технологии

- Python 3
- Flask
- SQLAlchemy (SQLite)
- HTML5, CSS3

## Установка

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/ribondareva/todo-app.git
cd todo-app
```

### 2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3. Запустите приложение:
```bash
python app.py
```

### 4. Откройте в браузере: http://localhost:5000