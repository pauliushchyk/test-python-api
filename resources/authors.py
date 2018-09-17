from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.author import Author


class AuthorsAPI(Resource):
    @orm.db_session
    def get(self):
        return jsonify([author.to_dict() for author in Author.select()])

    @orm.db_session
    def post(self):
        info = json.loads(request.data)
        parse = info['author']

        try:
            result = Author(
                first_name=parse['first_name'],
                last_name=parse['last_name'],
            )

            orm.commit()

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception
