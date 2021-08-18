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
        if self._connection is not None:
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

    def insert_user(self, username, email, password):
        """
        Insert a user into the database.

        Args:
            username (str): The name of the user
            email    (str): The email of the user
            password (str): The password of the user

        Returns:
            None

        """
        query_string = "insert into users(username, email, password) values(?, ? ,?)"
        query = self.cursor.execute(query_string, (username, email, password))
        self._connection.commit()
        # return query.fetchall()


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

    def raw_query(self, query_string):
        """
        Execute a raw SQL statement for testing purposes.

        !!! NOT SECURE !!!

        Args:
            query_string (str): The sql query.

        Returns:
            list. A single row if value is found. An empty list otherwise.
        """
        query = self.cursor.execute(query_string)
        return query.fetchone()

    def __del__(self):
        self.close()


