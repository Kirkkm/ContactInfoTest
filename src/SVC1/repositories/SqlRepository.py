import mysql.connector
from mysql.connector import Error


class SqlRepository:
    def __init__(self, hostname: str, username: str, password: str, db: str):
        try:
            connection = mysql.connector.connect(
                host=hostname, user=username, password=password, database=db
            )
            print(f"successfully connected to {hostname}")
        except Error as e:
            print("encountered error")
            print("=================")
            print(e)
        self.connection = connection

    def insert(self, insertStatement: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(insertStatement)
        self.connection.commit()

    def table_exist(self, table: str) -> bool:
        table_cursor = self.connection.cursor()
        table_cursor.execute("SHOW TABLES")
        return table in table_cursor

    def create_table(self, statement: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(statement)
