from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:

     
     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
     MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
     SECRET_KEY = os.environ.get('SECRET_KEY')
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:melo@localhost/watchlist'
     UPLOADED_PHOTOS_DEST ='app/static/photos'
     MAIL_SERVER = 'smtp.googlemail.com'
     MAIL_PORT = 587
     MAIL_USE_TLS = True
     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production configuratiion child class
    '''
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:melo@localhost/watchlist_test'
    '''
    development configuration child class
    '''
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:melo@localhost/watchlist'

    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}