# Тестовое задание: Веб-сервис для управления движением денежных средств (ДДС)

В фреймворке Django создан проект d_d_s.  
Создание виртуального окружения

    python -m venv .venv
    source .venv/bin/activate  # На Linux/Mac
    # или
    .\.venv\Scripts\activate  # На Windows

Структура папок  
Серийный номер тома: 6620-B5F1 


    C:.  
    ├───d_d_s  
    │   └───__pycache__  
    ├───site_ddsapp  
    │   ├───migrations  
    │   │   └───__pycache__  
    │   ├───static  
    │   │   └───site_ddsapp  
    │   │       ├───css  
    │   │       └───js  
    │   ├───templates  
    │   │   └───site_ddsapp  
    │   └───__pycache__  
    └───templates  

Технологии

Python 3.11+  
Django 5.0+  
SQLite (может быть заменена на   PostgreSQL, MySQL и др.)
HTML/CSS/JavaScript (Bootstrap 5) 

Настройка базы данных  

    python manage.py migrate

Создание администратора (опционально)  

    python manage.py createsuperuser


Запуск сервера разработки

    python manage.py runserver

После этого приложение будет доступно по адресу http://127.0.0.1:8000/.

Из тех задания сделан макет страниц HTML(создан базовый макет)

Созданы таблицы, создан супер пользователь

Созданы вьюшки-функции 

    name='create_page'
    name='edit_page'
    name='list_status'
    name='list_type'
    name='list_category'
    name='create_status'
    name='directory_management'
    name='create_type'
    name='create_category'

На HTML страницах реализованы простенькие форма-ввода в бз(тип , статус) 