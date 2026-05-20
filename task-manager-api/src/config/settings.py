import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me-in-production')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///tasks.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '5000'))
EMAIL_USER = os.environ.get('EMAIL_USER', '')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
