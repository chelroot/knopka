# knopka

Создание с ноля

Запустите консоль

Перейдите в папку, в которой будет распологаться django-проект

Выполните команду:

django-admin.py3 startproject knopka

cd knopka

[vova@dom rasb]$ python3 manage.py startapp mainapp

[vova@dom knopka]$ python3 manage.py makemigrations

[vova@dom knopka]$ python3 manage.py migrate

[vova@dom knopka]$ python manage.py shell

In [1]: from mainapp.models import *

In [2]: knopka = Knopka();knopka.name  = 'Testorg';knopka.save()

[vova@dom knopka]$ export DJANGO_SETTINGS_MODULE=knopka.settings
