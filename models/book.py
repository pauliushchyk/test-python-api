from pony import orm
from db import db
from author import Author


class Book(db.Entity):
    _table_ = 'books'

    id = orm.PrimaryKey(int, auto=True)

    name = orm.Required(str)
    description = orm.Optional(str)
    pages = orm.Required(int)
    image = orm.Optional(str)

    author = orm.Required(Author)

    genres = orm.Set("Genre")
