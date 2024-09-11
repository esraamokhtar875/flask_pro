from sqlalchemy.testing.plugin.plugin_base import config
import os

class Config:
    SECRET_KEY= os.urandom(35)



class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class ProductioConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = 'postgresql://itiuser:246@localhost:5432/library'


config_options = {
    'pro': ProductioConfig,
    'dev': DevelopmentConfig,
}