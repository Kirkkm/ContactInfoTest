import configparser
from pydantic import BaseModel
from src.SVC1.interfaces.IRepository import IRepository
from src.SVC1.repositories.SqlRepository import SqlRepository


class DataRepoBase[T: BaseModel](IRepository):
    """Base class for data repositories"""

    def __init__(self, table: str, create_table_statement: str):

        self.create_table_statement = create_table_statement
        self.table = table
        self.db_connect()

        # checks if the table already exist, if not we create it
        if self.table_exist(table) is False:
            self.create_table()

    def db_connect(self) -> None:
        """Sets up the connection to the database"""

        # config set up
        config = configparser.ConfigParser()
        config.read("config.ini")

        host = config.get("Database", "host")
        port = config.get("Database", "port")
        username = config.get("Database", "username")
        password = config.get("Database", "password")
        db = config.get("Database", "db")

        hostname = f"{host}:{port}"

        # Sql connection
        self.sql_repo = SqlRepository(hostname, username, password, db)

    def table_exist(self, table: str) -> bool:
        return self.sql_repo.table_exist(table)

    def create_table(self) -> None:
        self.sql_repo.create_table(self.create_table_statement)

    def delete(self, unique_id: str) -> None:
        raise NotImplementedError

    def get(self, unique_id: str) -> T:
        raise NotImplementedError

    def insert(self, data: T) -> None:
        shape = data.model_dump()
        columns = []
        values = []
        for key, value in shape.items():
            columns.append(key)
            values.append(value)

        insert_statement = (
            f"INSERT INTO ContactInfo {tuple(columns)} VALUES {tuple(values)}"
        )

        self.sql_repo.insert(insert_statement)

    def update(self, unique_id: str, data: T) -> None:
        raise NotImplementedError
