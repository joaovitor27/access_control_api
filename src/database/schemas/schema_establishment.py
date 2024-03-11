from pydantic import BaseModel

from src.database.schemas.schema_address import Address


class EstablishmentBase(BaseModel):
    name: str
    cnpj: str
    address: Address
    phone: str
    email: str

    class Config:
        orm_mode = True


class Establishment(EstablishmentBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class EstablishmentCreate(EstablishmentBase):
    pass


class EstablishmentUpdate(EstablishmentBase):
    pass


class EstablishmentDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True


def update_forward_refs_establishment():
    Establishment.update_forward_refs()
    EstablishmentBase.update_forward_refs()
    EstablishmentCreate.update_forward_refs()
    EstablishmentUpdate.update_forward_refs()
    EstablishmentDelete.update_forward_refs()
