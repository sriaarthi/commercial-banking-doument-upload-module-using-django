"# commercial-banking-doument-upload-module-using-django" 

Django-rest-framework-react : (ref: https://github.com/wsvincent/django-rest-framework-react-tutorial)

Backend setup: (ref: https://djangoforbeginners.com/initial-setup/)

1. Dowload and install python 3
Download the installer and make sure to click the Add Python to PATH option, which will let use use python directly from the command line.

2. Virtual Env 
Pipenv is similar to npm and yarn from the JavaScript/Node ecosystem: it creates a Pipfile containing software dependencies and a Pipfile.lock for ensuring deterministic builds. “Determinism” means that each and every time you download the software in a new virtual environment, you will have exactly the same configuration.
The end result is that we will create a new virtual environment with Pipenv for each new Django Project.
To install Pipenv we can use pip3 which HomeBrew automatically installed for us alongside Python 3.

$ pip3 install pipenv

3. Install Django

$ pipenv install django==2.2.5

If you look within our directory there are now two new files: Pipfile and Pipfile.lock. We have the information we need for a new virtual environment but we have not activated it yet. Let’s do that with pipenv shell.

$ pipenv shell

4. Create a new Django project called commercial-banking with the following command. Don’t forget that period . at the end.

(django-_0NWdoUR) $ django-admin startproject commercial_banking .

5. let’s confirm everything is working by running Django’s local web server.

(django-_0NWdoUR) $ python manage.py runserver
If you visit http://127.0.0.1:8000/ you should see the Django welcome page.

If it throws this error ->  Error: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions, try to run the server in a different port

(django-_0NWdoUR) $ python manage.py runserver 127.0.0.1:7000
Now if you visit http://127.0.0.1:7000/ you should see the Django welcome page.

Version Control:

Download from https://gitforwindows.org/ & install git.

Editor:

Download visual studio code and install it.

Frontend setup:


Softwares used:

 - python3.8.0,
 - Editor: VScode
 - DB: microsoft visual c++ 2015-2019 redistributable (x86) 14.24.28127,postgresql, pgadmin, psycopg2(It's a postgres database adapter which connects with python), 

Database Credentials: 
posgresSQL :
DB name: banking
password: 1234
port: 5432


####

# Local Setup

Python 3 and [Pipenv](https://docs.pipenv.org/) need to already be installed. If you need more complete local dev instructions, [see here](https://djangoforbeginners.com/initial-setup/).

## Backend

Install the `Pipenv` packages and start a new shell. Then `cd` into the `backend` directory and run the local server.

```
$ cd backend
$ pipenv install
$ pipenv shell
(backend) $ ./manage.py runserver
```

You can see the API now at [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api).

####

$pip install psycopg2
// This cmd installs psycopg2 through pip, which is the adapter that connects postgres database with the python code.

$python manage.py makemigrations
// This cmd will create the file 0001_initial.py in your module's(here frontend) migration folder. The file contains the create model(here customer) function().

$python manage.py sqlmigrate frontend 0001
// This cmd creates the table(here frontend_customer) with the SQL command itslef.

$python manage.py migrate
// This cmd will migrate and creates the table in the postgres DB

To create superuser :
$python manage.py createsuperuser
// This cmd will ask for the name, email and password
// admin name: sri 
// email: connect@sri.com
// password: 1234

If not sure about any commands, go for help command :
$python manage.py help
