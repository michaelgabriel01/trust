# trust
    A Simple Register WebAPP
    This app generate a unique secret key for any registered user.
    The secret keys are generated with the user's CPF (Brazilian Identification Number). 
    The app also generate a personalize link for every user. The links are generated with
    the user's host(user's computer IP address or domain name) plus the user's CPF. 
    Registration is done by filling out a form(for clients) or through the admin 
    interface(for administrator(s)). This app is easily extendable.

# Installation and setup
    First clone the project.
    Then, go ahead and use the following commands
    cd trust/
    virtualenv env -p python3
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py migrate 

# Test
    python manage.py test

# Environment
    Computer Sony Vaio CORE i5
    O.S Ubuntu 18.04lts
    Editor  SublimeText
    Python version  3.6.7
    Django version  2.1.3

# Basic Commands
    To create a superuser account, use this command::
    $ python manage.py createsuperuser

# Deployment
Deployed to heroku 
https://trust-register.herokuapp.com/
