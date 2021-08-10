import sqlite3
import pprint

class Database(object):
    """
    Database class that connects to an sqlite3 instance.

    :param str name: The name of the database - defaults to 'db.sqlite'

    """
    def __init__(self, db_name = 'db.sqlite'):
        self._connection = sqlite3.connect(db_name, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        self.cursor = self._connection.cursor()

    def close(self):
        """Close the connection to the database."""
        self._connection.close()

    def all(self, table_name):
        queryString = "select * from " + table_name
        query = self.cursor.execute(queryString)
        return query.fetchall()
