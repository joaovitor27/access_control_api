from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.database.database import get_db
from src.database.repositories.repository_address import RepositoryAddress
from src.database.schemas import schema_address

router = APIRouter()


@router.get('/address', status_code=status.HTTP_200_OK, response_model=List[schema_address.Address])
async def list_address(page: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    return RepositoryAddress(session).list(page, limit)
