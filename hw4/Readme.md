## Создаем и активируем виртуальное окружение
`python3 -m venv env`
`source env/bin/activate`

## Создаем проект Django
`pip install django`

`django-admin startproject films`

## Запускаем сервер
`python manage.py runserver`

## Создание приложения
`python manage.py startapp films`

`python manage.py startapp users`

## Выполнение миграций
`python manage.py migrate`

## Создание суперпользователя (для входа в админку)
`python manage.py createsuperuser`