import mysql.connector
from mysql.connector import Error

class SqlRepository:
    def __init__(self, hostname: str, username: str, userPass: str, db: str):
        connection = None
        try:
            connection = mysql.connector.connect(host = hostname, user = username, password = userPass, database = db)
            print(f'successfully connected to {hostname}')
        except Error as e:
            print('encountered error')
            print('=================')
            print(e)
        self.connection = connection

    def insert(self, insertQuery):
        cursor = self.connection.cursor()
        cursor.execute(insertQuery)
        self.connection.commit()