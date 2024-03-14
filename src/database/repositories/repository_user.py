from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import model_user
from src.database.schemas import schema_user


class RepositoryUser:

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schema_user.UserCreate):
        user = (
            model_user.User(
                street=user.street, postal_code=user.postal_code, number=user.number,
                neighborhood=user.neighborhood, city=user.city, state=user.state,
                complement=user.complement, country=user.country
            )
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def list(self, page: int, limit: int):
        result = select(model_user.User).offset(page).limit(limit)
        return self.session.execute(result).scalars().all()
