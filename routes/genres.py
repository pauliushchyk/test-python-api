from flask import Blueprint
from flask_restful import Api

genres_blueprint = Blueprint('genres', __name__)
genres_blueprint_api = Api(genres_blueprint)

from resources.genre import GenreAPI
from resources.genres import GenresAPI

genres_blueprint_api.add_resource(GenresAPI, '/genres')
genres_blueprint_api.add_resource(GenreAPI, '/genres/<int:id>')
