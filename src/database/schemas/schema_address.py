from pydantic import BaseModel

from src.database.enums.states_federation_enum import StatesFederation


class AddressBase(BaseModel):
    street: str
    number: str
    complement: str
    neighborhood: str
    city: str
    state: StatesFederation
    country: str
    postal_code: str

    class Config:
        orm_mode = True


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True


class AddressCreate(AddressBase):
    pass


class AddressUpdate(AddressBase):
    pass


class AddressDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True


def update_forward_refs_address():
    Address.update_forward_refs()
    AddressBase.update_forward_refs()
    AddressCreate.update_forward_refs()
    AddressUpdate.update_forward_refs()
    AddressDelete.update_forward_refs()
