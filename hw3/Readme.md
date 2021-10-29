# Веб-сервер
## Установка и настройка nginx
### Установка nginx (Ubuntu 20.04)
`sudo apt install nginx`
### Работа с nginx
Запуск - `sudo systemctl start nginx`

Перезапуск - `sudo systemctl restart nginx`

Остановка - `sudo systemctl stop nginx`
### Добавление своего config файла
Создаем server.conf 
`sudo touch /etc/nginx/sites-available/server.conf`

Редактируем server.conf с помощью текстового редактора

Создаем символическую ссылку на server.conf 
`sudo ln -s /etc/nginx/sites-available/server.conf /etc/nginx/sites-enabled/`
### Создание и активация виртуального окружения
Создание (в папке с проектом) - `python3 -m venv env`

Активация - `source env/bin/activate`
### Установка gunicorn
`pip install gunicorn`
### Запуск gunicorn (с 4 рабочими процессами)
`gunicorn --workers 4 wsgi_app:app`
### Другие команды для gunicorn 
Запуск в фоновом режиме - `gunicorn --workers 4 wsgi_app:app &`

Перевод в обычный режим - `fg`

Остановка (в обычном режиме) - `Ctrl+Z`

Завершение (в обычном режиме) - `Ctrl+C`
### Примеры запросов через браузер или консоль
Получение статических файлов (от nginx)

`http://localhost:9999/get_static/airbus.jpeg`

`http://localhost:9999/get_static/boeing.jpg`

`http://localhost:9999/get_static/boeing2.png`

`http://localhost:9999/get_static/my_example.html`

`http://localhost:9999/get_static/man.gif`

Проверка wsgi приложения

`http://127.0.0.1:8000/test?a=1&b=2`

Проверка работы nginx в качестве прокси-сервера (запущен nginx и gunicorn)

`http://127.0.0.1:9999/API/test_proxy?a=1&b=2`
### Замеры производительности
Установка apache-utils2 

`sudo apt install apache2-utils`

Сохранение результатов в файлы

`ab -k -c 4 -n 5000 'http://localhost:9999/get_static/boeing.jpg' > load_test_results/nginx_test.ab`

`ab -k -c 4 -n 5000 'http://127.0.0.1:8000/test1?a=1&b=2' > load_test_results/gunicorn_test.ab`

`ab -k -c 4 -n 5000 'http://localhost:9999/API/proxy?a=1&b=2' > load_test_results/nginx_proxy_test.ab`

Отказ системы

`ab -k -c 400 -n 10000 'http://localhost:9999/API/proxy?a=1&b=2'`
