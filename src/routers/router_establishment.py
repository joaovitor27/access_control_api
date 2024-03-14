from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.database.database import get_db
from src.database.repositories.repository_establishment import RepositoryEstablishment
from src.database.schemas import schema_establishment

router = APIRouter()


@router.get('/establishments', status_code=status.HTTP_200_OK, response_model=List[schema_establishment.Establishment])
async def list_establishment(page: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    return RepositoryEstablishment(session).list(page, limit)
