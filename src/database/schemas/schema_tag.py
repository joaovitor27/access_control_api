from pydantic import BaseModel


class TagBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    pass


class TagDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True


def update_forward_refs_tag():
    Tag.update_forward_refs()
    TagBase.update_forward_refs()
    TagCreate.update_forward_refs()
    TagUpdate.update_forward_refs()
    TagDelete.update_forward_refs()
