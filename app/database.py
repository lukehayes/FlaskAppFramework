import sqlite3

class Database(object):
    """
    Database class that connects to an sqlite3 instance.

    :param str name: The name of the database - defaults to 'database.db'

    """
    def __init__(self, db_name = "database.db"):
        self._connection = sqlite3.connect(db_name)
