from SVC1.types.ContactInfo import ContactInfo
from SVC1.interfaces.IDataRepo import IDataRepo
from mysql.connector.abstracts import MySQLCursorAbstract

# TODO: add an init statement to check if the table exist, if not create it
class ContactInfoRepo(IDataRepo):
    def __init__(self):
        
        pass

    def tableExist(self, table: str) -> bool:
        tableCursor = self.cursor.execute('SHOW TABLES')
        return table in tableCursor

    def createTable():
        '''
        create table ContactInfo
        (
            id int auto_increment
            Name        TEXT     not null,
            DateOfBirth DATE     null,
            PhoneNumber TEXT     not null,
            Email       TEXT     not null,
            Comments    LONGTEXT null
        );
        '''

    def insertContactInfo(contact: ContactInfo) -> str:
        return f'INSERT into ContactInfo (`Name`, `DateOfBirth`, `PhoneNumber`, `Email`, `Comments` ) VALUES (\'{contact.name}\', \'{contact.dateOfBirth}\', \'{contact.phoneNumber}\', \'{contact.email}\', \'{contact.comments}\');'