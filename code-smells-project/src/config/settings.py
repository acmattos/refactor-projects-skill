import os

SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
DATABASE_URL = os.environ.get("DATABASE_URL", "loja.db")
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
