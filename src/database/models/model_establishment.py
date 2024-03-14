from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database.database import Base


class Establishment(Base):
    __tablename__ = "establishment"

    id = Column(Integer, primary_key=True)
    cnpj = Column(String, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address", foreign_keys=[address_id], back_populates="establishment")

    user = relationship("User", back_populates="establishment")
