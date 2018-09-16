from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.genre import Genre


class GenresAPI(Resource):
    @orm.db_session
    def get(self):
        return jsonify([genre.to_dict() for genre in Genre.select()])

    @orm.db_session
    def post(self):
        info = json.loads(request.data)
        parse = info['genre']

        try:
            result = Genre(
                name=parse['name'],
            )

            orm.commit()

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception
