from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import model_tag
from src.database.schemas import schema_tag


class RepositoryTag:

    def __init__(self, session: Session):
        self.session = session

    def create(self, tag: schema_tag.TagCreate):
        tag = (
            model_tag.Tag(
                street=tag.street, postal_code=tag.postal_code, number=tag.number,
                neighborhood=tag.neighborhood, city=tag.city, state=tag.state,
                complement=tag.complement, country=tag.country
            )
        )

        self.session.add(tag)
        self.session.commit()
        self.session.refresh(tag)
        return tag

    def list(self, page: int, limit: int):
        result = select(model_tag.Tag).offset(page).limit(limit)
        return self.session.execute(result).scalars().all()
