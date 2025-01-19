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
├── learning_platform/          
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── courses/    
│   ├── management/
│   │   └── commands/    
│   │       └── wait_for_db.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── templatetags/
│   │   ├── course_tags.py
│   │   └── __init__.py
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
│   │    ├── topic_form.html
│   │    └── topic_rate.html
│   └── registration/
│        ├── login.html
│        └── register.html
│
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── venv/
