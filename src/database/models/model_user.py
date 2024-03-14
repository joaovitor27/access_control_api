from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    cell_phone = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    tag_id = Column(Integer, ForeignKey("tag.id"))
    establishment_id = Column(Integer, ForeignKey("establishment.id"))
    address_id = Column(Integer, ForeignKey("address.id"))

    tag = relationship("Tag", back_populates="user", foreign_keys=[tag_id])
    establishment = relationship("Establishment", back_populates="user", foreign_keys=[establishment_id])
    address = relationship("Address", back_populates="user", foreign_keys=[address_id])
