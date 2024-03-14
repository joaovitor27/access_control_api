from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.database.database import get_db
from src.database.repositories.repository_tag import RepositoryTag
from src.database.schemas import schema_tag

router = APIRouter()


@router.get('/tags', status_code=status.HTTP_200_OK, response_model=List[schema_tag.Tag])
async def list_tag(page: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    return RepositoryTag(session).list(page, limit)
