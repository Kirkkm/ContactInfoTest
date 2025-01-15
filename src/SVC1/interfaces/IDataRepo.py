from abc import ABC, abstractmethod
import configparser
from ..repositories.SqlRepository import SqlRepository

class IDataRepo(ABC):
    def __init__(self, table: str):
        
        # config set up
        config = configparser.ConfigParser()
        config.read('config.ini')

        host = config.read('Database', 'host')
        port = config.read('Database', 'port')
        username = config.read('Database', 'username')
        password = config.read('Database', 'password')
        db = config.read('Database', 'db')

        hostname = f'{host}:{port}'

        # Sql connection
        self.sqlRepo = SqlRepository(hostname, username, password, db)

        # checks if the table already exist, if not we create it
        if self.tableExist(table) == False:
            self.createTable(table)

    @property
    def tableExist(self, table: str) -> bool:
        return self.sqlRepo.checkTable(table)
    
    @abstractmethod
    def createTable(self, statement: str):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

