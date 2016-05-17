## List command a lession meetup


**_Lession 1_**

Create folder project

``
 $mkdir myproject
``

Install environment

``
  $virtualenv env
``

``
  $source env/bin/active
``

``
  $pip install -r requirement.txt
``

Create project

``
 $django-admin startproject djangoblog
``


Create apps

``
  $cd djangoblog
``

``
  $python manage.py startapp article
``

`` 
  $python manage.py startapp category
``

``
  $python manage.py startapp contact
``

Makemigrations

``
      $python manage.py makemigrations
``

Migrate

`` 
  $python manage.py migrate
``

Run Server

`` 
  $python manage.py runserver
``

Django shell

``
  $python manage.py shell
``

Create superuser

``
  $python manage.py createsuperuser
``
