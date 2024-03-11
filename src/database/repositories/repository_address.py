from fastapi import HTTPException, status
from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.database.models import model_address
from src.database.schemas import schema_address


class RepositoryAddress:

    def __init__(self, db: Session):
        self.session = db

    def create(self, address: schema_address.AddressCreate):
        db_address = (
            model_address.Address(
                street=address.street, postal_code=address.postal_code, number=address.number,
                neighborhood=address.neighborhood, city=address.city, state=address.state,
                complement=address.complement, country=address.country
            )
        )

        self.session.add(db_address)
        self.session.commit()
        self.session.refresh(db_address)
        return db_address

    def list(self, id_owner: int):
        result = select(model_address.Address).where(model_address.Address.user.id == id_owner)
        return self.session.execute(result).scalars().all()

    def get(self, id_address: int, owner_id: int):
        result = (select(model_address.Address)
                  .where(model_address.Address.id == id_address and model_address.Address.user.id == owner_id))
        return self.session.execute(result).scalars().first()

    def delete(self, id_address: int, owner_id: int):
        if not self.get(id_address, owner_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")

        result = (delete(model_address.Address)
                  .where(model_address.Address.id == id_address and model_address.Address.user.id == owner_id))
        self.session.execute(result)
        self.session.commit()

    def update(self, id_address: int, address: schema_address.AddressUpdate, owner_id: int):
        if not self.get(id_address, owner_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")

        result = (update(model_address.Address)
                  .where(model_address.Address.id == id_address and model_address.Address.user.id == owner_id)
                  .values(street=address.street, postal_code=address.postal_code, number=address.number,
                          neighborhood=address.neighborhood, city=address.city, state=address.state,
                          complement=address.complement, country=address.country))
        self.session.execute(result)
        self.session.commit()
