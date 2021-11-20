## Создаем и активируем виртуальное окружение
`python3 -m venv env`
`source env/bin/activate`

## Создаем проект Django
`pip install django`

`django-admin startproject films`

## Запускаем сервер
`python manage.py runserver`

## Создание приложений
`python manage.py startapp cars`

`python manage.py startapp users`

`python manage.py startapp makers`

## Работа с БД

Установка

`sudo apt install postgresql`

Вход под именем суперпользователя

`sudo -u postgres psql`

Создание пользователя

`create user vladislav with password '...';`

Создание базы данных

`create database hellcar owner vladislav;`

## Миграции

Подготовка миграций

`python manage.py makemigrations`

Применение миграций

`python manage.py migrate`

## Создание суперпользователя (для входа в админку)
`python manage.py createsuperuser`

## Для наполнения таблиц из psql

`insert into users_user(login, email) values ('SushkaVlad', 'vladislav2908@gmail.com');`

`insert into automakers_automaker(name, foundation_year, location, comment) values ('BMW', 1916, 'Munich, Germany','manufacturer of luxury vehicles and motorcycles');`

`insert into cars_car(make_id, model, type_of_drive, price, year, comment, creator_id) values (1, 'X5 F15', '4WD','15000','1999-2021', 'Car of dream', 11);`