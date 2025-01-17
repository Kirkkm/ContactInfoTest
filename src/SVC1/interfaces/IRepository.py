from abc import ABC, abstractmethod
from pydantic import BaseModel


class IRepository[T: BaseModel](ABC):
    """Interface for repositories"""

    @abstractmethod
    def db_connect(self) -> None:
        """Sets up the connection to the database"""
        pass

    @abstractmethod
    def table_exist(self, table: str) -> bool:
        """Checks if a table exist or not

        Args:
            table (str): name of the table

        Returns:
            bool: returns if the table is present or not
        """
        pass

    @abstractmethod
    def create_table(self) -> None:
        """Creates a table"""
        pass

    @abstractmethod
    def delete(self, unique_id: str) -> None:
        """Deletes row from the table

        Args:
            unique_id (str): identifier used to find and delete the row
        """
        pass

    @abstractmethod
    def get(self, unique_id: str) -> T:
        """Gets the data from the table

        Args:
            unique_id (str): identifier used to find the data

        Returns:
            T: data from the table
        """
        pass

    @abstractmethod
    def insert(self, data: T) -> None:
        """Inserts data into the table

        Args:
            data (T): data to be inserted
        """
        pass

    @abstractmethod
    def update(self, unique_id: str, data: T) -> None:
        """Updates the specified record in the table

        Args:
            unique_id (str): identifier used to find the data
            data (T): data used to update the record
        """
        pass
