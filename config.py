import os

SECRET_KEY = os.urandom(32)
PASSWORD = os.getenv("PASSWORD")
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{PASSWORD}@localhost:5432/fyurrapp'
