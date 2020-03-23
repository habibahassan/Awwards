## AWwARDS
## By ** Habiba **
## Description
An application that will allow a user to post a project he/she has created and get it reviewed by his/her peers.
## USER STORIES
 1.Register and Sign in to the application. 
 2.Upload projects to the application. 
 3.See my profile with all my pictures. 
  4.Review the projects on my timeline. 5.Like or Save and leave a comment on it.

## Prerequisites
1.Ubuntu Software
2.Python3.6
3.Postgres
4.python virtualenv
## Clone the Repo
Run the following command on the terminal: git clone https://github.com/habibahassan/Awwards.git
## Activate virtual environment
Activate virtual environment using python3.6 as default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
psql
CREATE DATABASE photos;
## .env file
Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'awar'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
## Run initial Migration
python3.6 manage.py makemigrations photos
python3.6 manage.py migrate
## Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

Known bugs
logout has a bit of an issue

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- Bootstrap 3
- JavaScript
## Support and contact details
Contact me on developer on halimaadan92@gmail.com for any comments, reviews or advice.

#  Licence
 licensed under the [MIT License](license)
 copyright(c) 20120 Awwards
