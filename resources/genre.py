from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.genre import Genre


class GenreAPI(Resource):
    @orm.db_session
    def get(self, id):
        try:
            if not Genre.exists(lambda genre: genre.id == int(id)):
                return None, 404

            return jsonify(Genre[int(id)].to_dict())

        except Exception as exception:
            return exception, 404

    @orm.db_session
    def put(self, id):
        try:
            if not Genre.exists(lambda genre: genre.id == int(id)):
                return None, 404

            info = json.loads(request.data)
            parse = info['genre']

            result = Genre[int(id)]
            result.set(
                name=parse['name'],
            )

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception

    @orm.db_session
    def delete(self, id):
        try:
            if not Genre.exists(lambda genre: genre.id == int(id)):
                return None, 404

            Genre[int(id)].delete()

            return None, 200

        except Exception as exception:
            return exception
