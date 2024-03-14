from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import model_establishment
from src.database.schemas import schema_establishment


class RepositoryEstablishment:

    def __init__(self, session: Session):
        self.session = session

    def create(self, address: schema_establishment.EstablishmentCreate):
        establishment = (
            model_establishment.Establishment(
                street=address.street, postal_code=address.postal_code, number=address.number,
                neighborhood=address.neighborhood, city=address.city, state=address.state,
                complement=address.complement, country=address.country
            )
        )

        self.session.add(establishment)
        self.session.commit()
        self.session.refresh(establishment)
        return establishment

    def list(self, page: int, limit: int):
        result = select(model_establishment.Establishment).offset(page).limit(limit)
        return self.session.execute(result).scalars().all()
