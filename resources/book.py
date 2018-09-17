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
        try:
            if not Book.exists(lambda book: book.id == int(id)):
                return None, 404

            return jsonify(Book[int(id)].to_dict())

        except Exception as exception:
            return exception, 404

    @orm.db_session
    def put(self, id):
        try:
            if not Book.exists(lambda book: book.id == int(id)):
                return None, 404

            info = json.loads(request.data)
            parse = info['book']

            result = Book[int(id)]
            result.set(
                name=parse['name'],
                description=parse['description'],
                pages=parse['pages'],
                image=parse['image'],
                author=Author[int(parse['author_id'])],
                genres=[genre
                        for genre
                        in Genre.select(lambda g: g.id in parse['genres'])]
            )

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception

    @orm.db_session
    def delete(self, id):
        try:
            if not Book.exists(lambda book: book.id == int(id)):
                return None, 404

            Book[int(id)].delete()

            return {}, 200

        except Exception as exception:
            return exception
