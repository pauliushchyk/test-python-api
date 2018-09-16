from flask import Flask
from flask_restful import Api, Resource

from models.db import db
from models.author import Author
from models.book import Book
from models.genre import Genre

app = Flask(__name__)
api = Api(app)


db.bind(provider='postgres', user='postgres', password='pgpassword',
        host='localhost', database='Books', port='5432')
db.generate_mapping(create_tables=True)


@app.errorhandler(404)
def not_found(e):
    return '', 404


from routes.authors import authors_blueprint
from routes.books import books_blueprint
from routes.genres import genres_blueprint

app.register_blueprint(authors_blueprint)
app.register_blueprint(books_blueprint)
app.register_blueprint(genres_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
