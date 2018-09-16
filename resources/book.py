from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.author import Author
from models.book import Book
from models.genre import Genre


class BookAPI(Resource):
    @orm.db_session
    def get(self, id):
        return jsonify(Book[int(id)].to_dict())

    @orm.db_session
    def put(self, id):
        info = json.loads(request.data)
        parse = info['book']

        try:
            result = Book[int(id)]
            result.set(
                name=parse['name'],
                description=parse['description'],
                pages=parse['pages'],
                image=parse['image'],
                author=Author[int(parse['authorId'])],
                genres=[genre
                        for genre
                        in Genre.select(lambda g: g.id in parse['genres'])]
            )

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception

    @orm.db_session
    def delete(self, id):
        Book[int(id)].delete()

        return {}, 200
