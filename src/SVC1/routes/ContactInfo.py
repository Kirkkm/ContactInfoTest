from fastapi import APIRouter, HTTPException
from src.SVC1.models.ContactInfo import ContactInfo
from src.SVC1.repositories.ContactInfoRepo import ContactInfoRepo

router = APIRouter(prefix="/ContactUs", tags=["/ContactUs"])
contact_info_repo = ContactInfoRepo()


@router.post("/")
def create_contact(contact: ContactInfo) -> ContactInfo:
    """Endpoint to create a Contact's Information

    Args:
        contact (ContactInfo): Data to be saved

    Returns:
        ContactInfo: The data being saved in a 200 response
    """
    contact_info_repo.insert(contact)
    return contact
