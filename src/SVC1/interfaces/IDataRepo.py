from abc import ABC, abstractmethod
import configparser
from src.SVC1.repositories.SqlRepository import SqlRepository


class IDataRepo[T](ABC):
    """Base class for data repositories"""

    def __init__(self, table: str):

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

        # checks if the table already exist, if not we create it
        if self.table_exist(table) is False:
            self.create_table(table)

    def table_exist(self, table: str) -> bool:
        """Checks if a table exist or not

        Args:
            table (str): name of the table

        Returns:
            bool: returns if the table is present or not
        """
        return self.sql_repo.table_exist(table)

    def create_table(self, statement: str) -> None:
        """Creates a table

        Args:
            statement (str): Statement to run to create a table in the db
        """
        self.sql_repo.create_table(statement)

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

    @abstractmethod
    def insert(self, data: T) -> None:
        """Inserts data into the table

        Args:
            data (T): data to be inserted
        """

    @abstractmethod
    def update(self, unique_id: str, data: T) -> None:
        """Updates the specified record in the table

        Args:
            unique_id (str): identifier used to find the data
            data (T): data used to update the record
        """
