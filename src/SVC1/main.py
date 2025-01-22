from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from src.SVC1.types.ContactInfo import ContactInfo
from src.SVC1.repositories.ContactInfoRepo import ContactInfoRepo

app = FastAPI()
contact_info_repo = ContactInfoRepo()

# TODO: update CORS logic to connect FE with BE
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# TODO: add validation
@app.post("/ContactUs", response_model=ContactInfo, status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactInfo) -> ContactInfo:
    """Endpoint to create a Contact's Information

    Args:
        contact (ContactInfo): Data to be saved

    Returns:
        ContactInfo: The data being saved in a 200 response
    """
    contact_info_repo.insert(contact)
    return contact
