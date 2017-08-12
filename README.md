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
/usr/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py:57: RuntimeWarning: SQLite received a naive datetime (2017-08-12 14:25:19.106937) while time zone support is active.
  RuntimeWarning)

Python 2.7.11 (default, Apr 15 2016, 13:09:43) 
Type "copyright", "credits" or "license" for more information.

IPython 4.0.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from mainapp.models import *

In [2]: knopka = Knopka();knopka.name  = 'Testorg';knopka.save()

[vova@dom knopka]$ export DJANGO_SETTINGS_MODULE=knopka.settings
