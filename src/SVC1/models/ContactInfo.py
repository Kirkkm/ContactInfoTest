from pydantic import BaseModel


class ContactInfo(BaseModel):
    Name: str
    DateOfBirth: str | None
    PhoneNumber: str
    Email: str
    Comments: str | None
