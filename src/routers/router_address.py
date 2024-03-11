from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.database.database import get_db
from src.database.repositories.repository_address import RepositoryAddress
from src.database.schemas import schema_address

router = APIRouter()


@router.post('/api/address', status_code=status.HTTP_201_CREATED, response_model=schema_address.Address)
async def create_address(address: schema_address.AddressCreate, session: Session = Depends(get_db)):
    return RepositoryAddress(session).create(address)
