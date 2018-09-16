from flask import jsonify, request
from flask_restful import Resource
import json
from pony import orm
from models.author import Author
from models.book import Book
from models.genre import Genre


class BooksAPI(Resource):
    @orm.db_session
    def get(self):
        return jsonify([book.to_dict() for book in Book.select()])

    @orm.db_session
    def post(self):
        info = json.loads(request.data)
        parse = info['book']

        try:
            result = Book(
                name=parse['name'],
                description=parse['description'],
                pages=parse['pages'],
                author=Author[int(parse['authorId'])],
                genres=[genre
                        for genre
                        in Genre.select(lambda g: g.id in parse['genres'])],
            )

            orm.commit()

            return jsonify(result.to_dict())

        except Exception as exception:
            return exception
