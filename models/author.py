from pony import orm
from db import db


class Author(db.Entity):
    _table_ = 'authors'

    id = orm.PrimaryKey(int, auto=True)

    first_name = orm.Required(str)
    last_name = orm.Required(str)

    books = orm.Set("Book")
