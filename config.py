import os

CSRF_ENABLED = True
SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
AWS_URI = os.environ['AWS_URI']