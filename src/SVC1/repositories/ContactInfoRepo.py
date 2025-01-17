from src.SVC1.types.ContactInfo import ContactInfo
from src.SVC1.interfaces.IDataRepo import IDataRepo


class ContactInfoRepo[ContactInfo](IDataRepo):
    """ContactInfo repository

    Args:
        IDataRepo (_type_): Abstract Base Class used for Contact Info
    """

    def __init__(self):

        table = "ContactInfo"
        create_table_statement = """
        create table ContactInfo
        (
            id int auto_increment
            Name        TEXT     not null,
            DateOfBirth DATE     null,
            PhoneNumber TEXT     not null,
            Email       TEXT     not null,
            Comments    LONGTEXT null
        );
        """

        super().__init__(table, create_table_statement)

        self.db_connect()

        # checks if the table already exist, if not we create it
        if self.table_exist(table) is False:
            self.create_table()
