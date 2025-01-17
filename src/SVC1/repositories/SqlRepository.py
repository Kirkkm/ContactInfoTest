import mysql.connector
from mysql.connector import Error


class SqlRepository:
    """A repository to interact with a MySql database"""

    def __init__(self, hostname: str, port: str, username: str, password: str, db: str):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=hostname, port=port, user=username, password=password, database=db
            )
            print(f"successfully connected to {hostname}")
        except Error as e:
            print("encountered error")
            print("=================")
            print(e)
            raise e
        self.connection = connection

    def insert(self, insert_statement: str) -> None:
        """Inserts data into a MySql database

        Args:
            insert_statement (str): Insert statement to be executed
        """
        cursor = self.connection.cursor()
        cursor.execute(insert_statement)
        self.connection.commit()

    def table_exist(self, table: str) -> bool:
        """Checks if a tables exists in the MySql database

        Args:
            table (str): Name of the table to check

        Returns:
            bool: Returns if a table exists or not
        """
        table_cursor = self.connection.cursor()
        table_cursor.execute("SHOW TABLES")
        for t in table_cursor:  # type: ignore
            if table in t:
                return True
        return False

    def create_table(self, statement: str) -> None:
        """Creates a table in the MySql database

        Args:
            statement (str): MySql state to run to create the new table
        """
        cursor = self.connection.cursor()
        cursor.execute(statement)
