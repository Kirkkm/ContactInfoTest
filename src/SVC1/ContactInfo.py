from pydantic import BaseModel

class ContactInfo(BaseModel):
    name: str
    dateOfBirth: str | None
    phoneNumber: str
    email: str
    comments: str | None