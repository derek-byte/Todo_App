Utilizes Django and SQLite

Start Django Project:
- django-admin startproject <name>

Migrate First Database:
cd todo
python3 manage.py migrate

Create First User:
cd todo
python3 manage.py createsuperuser

Create Basic App:
cd todo
python3 manage.py startapp <name>

Create Model:
python3 manage.py makemigrations

Run App:
cd todo
python3 manage.py runserver