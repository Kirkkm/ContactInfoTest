from sqlalchemy import true
from sqlmodel import SQLModel, Field


class ContactInfo(SQLModel, table=true):
    id: int | None = Field(primary_key=True, default=None)
    Name: str
    DateOfBirth: str | None = None
    PhoneNumber: str
    Email: str
    Comments: str | None = None
