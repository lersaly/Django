Сайт доступен по адресу:

https://learning.dizeldigital.ru/login/?next=/

Панель админа:

https://learning.dizeldigital.ru/admin/login/?next=/admin/%3Fnext%3D/

Можно использовать докер контейнер:

docker pull lersaly/learning_platform:latest

docker run -p 8000:8000 lersaly/learning_platform:latest

Проект содержит следующую структуру:
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
│   │       ├── __init__.py
│   │       ├── wait_for_db.py
│   │       └── create_superuser.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── templatetags/
│   │   ├── course_tags.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
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
│   │    ├── enrolled_students.html
│   │    ├── topic_delete.html
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

# Общее описание проекта

Данный проект представляет собой платформу для онлайн обучения, разработанную с использованием фреймворка Django. В основе системы лежит концепция двух типов пользователей: преподаватели, которые могут создавать и управлять учебными курсами, и студенты, имеющие возможность записываться на эти курсы и оценивать качество представленного материала.

# Функциональные возможности

Система реализует полноценный процесс онлайн обучения, начиная с регистрации пользователей и заканчивая оценкой эффективности обучения. При регистрации пользователь может выбрать роль преподавателя или студента, что определяет его дальнейшие возможности в системе. 

Преподаватели получают доступ к инструментам создания и управления курсами. Каждый курс состоит из упорядоченных тем, которые преподаватель может добавлять и редактировать. В рамках каждой темы преподаватель размещает учебный материал, который будет доступен студентам после их записи на курс. Особое внимание уделено системе обратной связи: преподаватели могут отслеживать среднюю оценку как по отдельным темам, так и по курсу в целом, что позволяет оценивать эффективность представления материала и при необходимости его корректировать.

Студенты имеют возможность просматривать список доступных курсов, записываться на интересующие их курсы и отписываться от них. После изучения каждой темы студенты оценивают качество представления материала по десятибалльной шкале, где 1 означает полное непонимание материала, а 10 - идеальное представление темы. Эта система оценивания помогает как преподавателям улучшать качество своих курсов, так и другим студентам ориентироваться при выборе курсов.

# Техническая реализация

Архитектура проекта построена на основе Django-приложений, где основная логика сосредоточена в приложении courses. База данных спроектирована с учетом всех необходимых связей между сущностями системы: пользователями, курсами, темами и оценками.

Модель данных включает в себя несколько ключевых сущностей. Курсы (Course) содержат основную информацию о учебном материале, включая название, описание и связь с создателем курса. Темы (Topic) представляют собой структурные единицы курса с собственным содержанием и порядковым номером. Система хранит информацию о записи студентов на курсы (StudentCourse) и их оценках материала (TopicRating). Профили пользователей (UserProfile) расширяют стандартную модель пользователя Django дополнительной информацией о роли пользователя.

Для упрощения разработки и развертывания проект контейнеризирован с использованием Docker. Это обеспечивает единообразное окружение разработки и упрощает процесс развертывания приложения. Docker-конфигурация включает все необходимые зависимости и настройки для корректной работы системы.


# Перспективы развития

Система спроектирована с учетом возможности дальнейшего расширения функционала. В будущем возможно добавление поддержки различных типов контента (видео, аудио), реализация более сложной системы отслеживания прогресса обучения, внедрение системы сертификации и расширение аналитических возможностей для преподавателей.

# Заключение

Разработанная платформа представляет собой полноценное решение для организации онлайн обучения. Она обеспечивает все необходимые инструменты как для создания и управления учебными материалами, так и для их изучения и оценки. Гибкая архитектура и современные технологии, использованные при разработке, позволяют легко поддерживать и развивать систему в соответствии с растущими потребностями пользователей.