from flask import Blueprint
from flask_restful import Api

authors_blueprint = Blueprint('authors', __name__)
authors_blueprint_api = Api(authors_blueprint)

from resources.author import AuthorAPI
from resources.authors import AuthorsAPI

authors_blueprint_api.add_resource(AuthorsAPI, '/authors')
authors_blueprint_api.add_resource(AuthorAPI, '/authors/<int:id>')
