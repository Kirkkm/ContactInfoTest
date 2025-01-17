from abc import ABC, abstractmethod
import configparser
from src.SVC1.repositories.SqlRepository import SqlRepository
from pydantic import BaseModel


class IDataRepo[T: BaseModel](ABC):
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
        """Checks if a table exist or not

        Args:
            table (str): name of the table

        Returns:
            bool: returns if the table is present or not
        """
        return self.sql_repo.table_exist(table)

    @abstractmethod
    def create_table(self) -> None:
        """Creates a table"""
        self.sql_repo.create_table(self.create_table_statement)

    @abstractmethod
    def delete(self, unique_id: str) -> None:
        """Deletes row from the table

        Args:
            unique_id (str): identifier used to find and delete the row
        """

    @abstractmethod
    def get(self, unique_id: str) -> T:
        """Gets the data from the table

        Args:
            unique_id (str): identifier used to find the data

        Returns:
            T: data from the table
        """

    def insert(self, data: T) -> None:
        """Inserts data into the table

        Args:
            data (T): data to be inserted
        """
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

    @abstractmethod
    def update(self, unique_id: str, data: T) -> None:
        """Updates the specified record in the table

        Args:
            unique_id (str): identifier used to find the data
            data (T): data used to update the record
        """
