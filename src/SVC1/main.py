from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.SVC1.types.ContactInfo import ContactInfo
from src.SVC1.repositories.ContactInfoRepo import ContactInfoRepo

app = FastAPI()
contact_info_repo = ContactInfoRepo()

origins = ["http://localhost:3000/", "http://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ContactUs")
def create_contact(contact: ContactInfo) -> ContactInfo:
    contact_info_repo.insert(contact)
    return contact
