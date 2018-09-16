from pony import orm
from db import db


class Author(db.Entity):
    _table_ = 'authors'

    id = orm.PrimaryKey(int, auto=True)

    firstName = orm.Required(str)
    lastName = orm.Required(str)

    books = orm.Set("Book")
