from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.database.database import get_db
from src.database.repositories.repository_user import RepositoryUser
from src.database.schemas import schema_user

router = APIRouter()


@router.get('/users', status_code=status.HTTP_200_OK, response_model=List[schema_user.User])
async def list_user(page: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    return RepositoryUser(session).list(page, limit)
