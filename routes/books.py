from flask import Blueprint
from flask_restful import Api

books_blueprint = Blueprint('books', __name__)
books_blueprint_api = Api(books_blueprint)

from resources.book import BookAPI
from resources.books import BooksAPI

books_blueprint_api.add_resource(BooksAPI, '/books')
books_blueprint_api.add_resource(BookAPI, '/books/<int:id>')
