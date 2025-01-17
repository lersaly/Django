Основные URL-адреса:

Главная страница: http://127.0.0.1:8000/
Админ-панель: http://127.0.0.1:8000/admin/
Вход в систему: http://127.0.0.1:8000/login/
Создание курса: http://127.0.0.1:8000/course/create/

Каждый файл играет свою роль:

settings.py: основные настройки проекта
urls.py: маршрутизация URL
models.py: определение структуры базы данных
views.py: логика обработки запросов
forms.py: формы для ввода данных
admin.py: настройки админ-панели
templates: HTML-шаблоны
static: CSS, JavaScript и медиафайлы

learning_platform/
│
├── learning_platform/          # Основной проект
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── courses/                    # Приложение
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   ├── courses/
│   │    ├── course_list.html
│   │    ├── course_form.html
│   │    ├── course_detail.html
│   │    └── topic_rate.html
│   └── registration/
│        ├── login.html
│        └── register.html
│
├── manage.py
├── requirements.txt
└── venv/