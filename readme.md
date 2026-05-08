

# How to create a Django project?

## Step 1
Create a folder for the project

## Step 2
Open in VS Code and open a terminal

## Step 3
Create a virtual environment for the project

    Mac OS: python3 -m venv venv
    Windows: python|py -m venv venv

## Step 4
Activate the virtual environment

    Mac OS: source venv/bin/activate
    Windows: .\venv\Scripts\activate

## Step 5
Install Django dependency

    Mac OS: pip3 install django
    Windows: pip install django

## Step 6
Run the startproject command to create the project settings

    Both OS: django-admin startproject NAME_OF_PROJECT .
    Note: replace NAME_OF_PROJECT with config or any other name

    Expected Output: two folders and a single file called **manage.py**


## step 7
 window: python manage.py runserver 
 
## step 8
Django command to create apps:

Windows: python manage.py startapp NAME_OF_THE_APP
Mac OS: python3 manage.py startapp NAME_OF_THE_APP

Django command to verify errors:
Python3 manage.py check


## step 9
Both os: prthon manage.py startopp mane_of_the _app

## models in Django

When we finish a model structure we need to run  these comand in order:

1. python manage.py makemigration
2. python manage.py migrate