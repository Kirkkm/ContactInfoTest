from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from SVC1.types.ContactInfo import ContactInfo
from SVC1.repositories.SqlRepository import SqlRepository
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
    insertSqlStatement: str = ''
    sqlRepository.insert(insertSqlStatement)
    return contact
