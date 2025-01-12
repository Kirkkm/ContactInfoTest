from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ContactInfo import ContactInfo
from SqlRepository import SqlRepository

app = FastAPI()
sqlRepository = SqlRepository('127.0.0.1','root','data','phennx')

origins = [
    'http://localhost:3000/',
    'http://localhost'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/ContactUs')
def createContact(contact: ContactInfo):
    insertSqlStatement: str = createSqlInsertStatement(contact)
    sqlRepository.insert(insertSqlStatement)
    return contact


def createSqlInsertStatement(contact: ContactInfo) -> str:
    return f'INSERT into ContactInfo (`Name`, `DateOfBirth`, `PhoneNumber`, `Email`, `Comments` ) VALUES (\'{contact.name}\', \'{contact.dateOfBirth}\', \'{contact.phoneNumber}\', \'{contact.email}\', \'{contact.comments}\');'