from flask import Blueprint

books_blueprint = Blueprint('books', __name__ , url_prefix='/books')

from app.book import views
