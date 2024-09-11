from flask import Flask
from flask_migrate import Migrate
from app.model import db
from app.config import config_options
from app.book import books_blueprint

def create_app(config_name='pro'):


   app =Flask(__name__)
   current_config = config_options[config_name]
   app.config.from_object(current_config)
   app.config.SQLALCHEMY_DATABASE_URI = current_config.SQLALCHEMY_DATABASE_URI

   db.init_app(app)
   migrate= Migrate(app,db)

   app.register_blueprint(books_blueprint)

   return  app


