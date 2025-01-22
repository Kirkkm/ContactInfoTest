import configparser
from pydantic import BaseModel
from src.SVC1.interfaces.IRepository import IRepository
from sqlmodel import create_engine, SQLModel, Session


class DataRepoBase[T: BaseModel](IRepository):
    """Base class for data repositories"""

    def __init__(self, table: str):

        # self.create_table_statement = create_table_statement
        self.table = table
        self.db_connect()

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

        # Sql connection
        db_url = f"mysql://{username}:{password}@{host}:{port}/{db}"
        self.engine = create_engine(db_url, echo=True)

    def create_table(self) -> None:
        SQLModel.metadata.create_all(self.engine)

    def delete(self, unique_id: str) -> None:
        raise NotImplementedError

    def get(self, unique_id: str) -> T:
        raise NotImplementedError

    def insert(self, data: T) -> None:
        Session(self.engine).add(data)
        Session(self.engine).commit()

    def update(self, unique_id: str, data: T) -> None:
        raise NotImplementedError
