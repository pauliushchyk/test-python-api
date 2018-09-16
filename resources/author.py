from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.author import Author


class AuthorAPI(Resource):
    @orm.db_session
    def get(self, id):
        return jsonify(Author[int(id)].to_dict())

    @orm.db_session
    def put(self, id):
        info = json.loads(request.data)
        parse = info['author']

        try:
            result = Author[int(id)]
            result.set(
                firstName=parse['firstName'],
                lastName=parse['lastName'],
            )

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception

    @orm.db_session
    def delete(self, id):
        Author[int(id)].delete()

        return {}, 200
