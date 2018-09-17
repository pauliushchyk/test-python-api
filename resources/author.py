from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.author import Author


class AuthorAPI(Resource):
    @orm.db_session
    def get(self, id):
        try:
            if not Author.exists(lambda author: author.id == int(id)):
                return None, 404

            return jsonify(Author[int(id)].to_dict())

        except Exception as exception:
            return exception, 404

    @orm.db_session
    def put(self, id):
        try:
            if not Author.exists(lambda author: author.id == int(id)):
                return None, 404

            info = json.loads(request.data)
            parse = info['author']

            result = Author[int(id)]
            result.set(
                first_name=parse['first_name'],
                last_name=parse['last_name'],
            )

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception

    @orm.db_session
    def delete(self, id):
        try:
            if not Author.exists(lambda author: author.id == int(id)):
                return None, 404

            Author[int(id)].delete()

            return None, 200

        except Exception as exception:
            return exception
