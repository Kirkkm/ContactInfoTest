from src.SVC1.types.ContactInfo import ContactInfo
from src.SVC1.repositories.DataRepoBase import DataRepoBase


class ContactInfoRepo[ContactInfo](DataRepoBase):
    """ContactInfo repository

    Args:
        IDataRepo (_type_): Abstract Base Class used for Contact Info
    """

    def __init__(self):

        table = "ContactInfo"
        create_table_statement = (
            "create table ContactInfo"
            "("
            "id int auto_increment"
            "Name        TEXT     not null,"
            "DateOfBirth DATE     null,"
            "PhoneNumber TEXT     not null,"
            "Email       TEXT     not null,"
            "Comments    LONGTEXT null"
            ");"
        )

        super().__init__(table, create_table_statement)
