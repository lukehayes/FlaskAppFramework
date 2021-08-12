import sqlite3
import pprint

class Database(object):
    """
    Database class that connects to an sqlite3 instance.
    """

    def __init__(self, db_name = 'db.sqlite'):
        """
        Constructor.

        Args:
            name (str): The name of the database - defaults to 'db.sqlite'.

        """
        self._connection = sqlite3.connect(db_name, check_same_thread=False)

        # Return results as objects
        self._connection.row_factory = sqlite3.Row

        self.cursor = self._connection.cursor()

    def close(self):
        """
        Close the connection to the database.

        Returns:
            None

        """
        self._connection.close()

    def all(self, table_name):
        """
        Run a select * on a specific table.

        Args:
            table_name (str): The name of the table.
            name       (str): The name of the database - defaults to 'db.sqlite'.

        Returns:
            list. Each row that is returned from the query.

        """
        queryString = "select * from " + table_name
        query = self.cursor.execute(queryString)
        return query.fetchall()

    def find(self, table_name, value):
        """
        Find a specific row from the database using a specified value.

        Args:
            table_name (str): The name of the table.
            value      (str): The value to search for.

        Returns:
            list. A single row if value is found. An empty list otherwise.

        """
        queryString = 'select * from {} where username = "{}" limit 1;'.format(table_name, value)
        query = self.cursor.execute(queryString)
        return query.fetchone()



