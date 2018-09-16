from pony import orm
from db import db


class Genre(db.Entity):
    _table_ = 'genres'

    id = orm.PrimaryKey(int, auto=True)

    name = orm.Required(str)

    books = orm.Set("Book")
