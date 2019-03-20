import os

base_dir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:123456@localhost/'
database_name = 'location_db'


class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    BCRYPT_HASH_PREFIX = 14
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECONDS = 3000
    BUCKET_AND_ITEMS_PER_PAGE = 25


class Config(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', postgres_local_base + database_name)
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 1
    AUTH_TOKEN_EXPIRY_SECONDS = 20
    BUCKET_AND_ITEMS_PER_PAGE = 4
