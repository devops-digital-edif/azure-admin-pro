import os
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env into os.environ

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    PROFILE_CONTAINER = 'profile-pictures'
    COURSE_CONTAINER = 'course-images'

