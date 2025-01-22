from src.SVC1.types.ContactInfo import ContactInfo
from src.SVC1.repositories.DataRepoBase import DataRepoBase


class ContactInfoRepo[ContactInfo](DataRepoBase):
    """ContactInfo repository

    Args:
        IDataRepo (_type_): Abstract Base Class used for Contact Info
    """

    def __init__(self):

        table = "ContactInfo"
        super().__init__(table)
