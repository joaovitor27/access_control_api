from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    cell_phone: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    is_active: bool
    tag_id: int
    establishment_id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True


def update_forward_refs_user():
    User.update_forward_refs()
    UserBase.update_forward_refs()
    UserCreate.update_forward_refs()
    UserUpdate.update_forward_refs()
    UserDelete.update_forward_refs()
