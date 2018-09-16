from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.genre import Genre


class GenreAPI(Resource):
    @orm.db_session
    def get(self, id):
        return jsonify(Genre[int(id)].to_dict())

    @orm.db_session
    def put(self, id):
        info = json.loads(request.data)
        parse = info['genre']

        try:
            result = Genre[int(id)]
            result.set(
                name=parse['name'],
            )

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception

    @orm.db_session
    def delete(self, id):
        Genre[int(id)].delete()

        return {}, 200
