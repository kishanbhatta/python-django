# Django is a free and open source Web framework.
# It is used by many sites, including Pinterest, PDS, Instagram,
# BitBucket, Washington Times, Mozilla, and more!

# Django was created in 2003 when the web developers at the Lawrence Journal-World
# newspaper started using Python for their development.
# The fact that is originated at a newspaper is important.
# Because the original developers were surrounded by writers, good written
# documentation is a key part of Django!
# This means you have excellent references to check on the official Django docs!
# Django has its own excellent basic tutorial where you are walked through creating a basic polling web app.
# The reason it is a poll also extends back to its newspaper roots!
# When encountering Django tutorials you will often read that you should create a virtual environment or an "venv"
# LEts talk abot what this is and how to use it!
# A virtual environment allows you to hav ea virtual installation of Python and packages on your computer.
# So why would you ever want or need this?
# Pythons packages change and get updated often!
# There are changes that break backwards compatibility.
# So what do you do if you want to test out new features but not break your web app?
# A virtual environment handler is included!

# Create virtual environment
# Activate virtual environment
# then start django admin
# $ django-admin startproject first_project
# It automatically create a files which contains
# __init__.py
    # This is a blank Python script that due to its special name lts's Python know that this directory can be treated as a package

# setting.py
    # This is where you will store all your project settings

# urls.py
    # This is a Python script that will store all the URL patterns for your project. Basically the different pages of your web application.

# wsgi.py
    # This is a Python Script that acts as the Web Server Gateway interface. It will later on help us deploy our web app to production

# manage.py
    # This is a Python script that we will use a lot It will be associates with many commands as we build our web app!

# Let's use manage.py now:
# $ python manage.py runserver
# copy and paste that url into your browser
# You should now see your very first web page being locally hosted on your computer.

# You should have also noticed a warning about migrations.
# This has to do with databases and how to connect them to Django

# What is migration?
# A migration allows you to move databases from one design to another,
# this is also reversible.
# So you can "migrate" your database
# We will touch back on this later, for now you can ignore this warning.

# To start the django project we have to first start the application
#   $ python manage.py startapp first_app
# It will create a folder called first_app which have multiple files
# Files and their values
#  __init__.py
    # This is a blank Python script that due to its special name let's
    # Python know that this directory can be treated as a package
#  admin.py
    # You can register your models here which Django will then use them with Django's admin interface.
#  apps.py
    # Here you can place application speciic configurations
# models.py
    # Here you store the application's data models
# tests.py
    # Here you can store test functions to test your code.
# views.py
    # This is where you have functions that handle request and return responses.
# Migration folder
    # This directory stores databases specific information as it relates to the models





