from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from src.database.database import Base
from src.database.enums.states_federation_enum import StatesFederation


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    number = Column(Integer, index=True)
    complement = Column(String, index=True)
    neighborhood = Column(String, index=True)
    city = Column(String, index=True)
    state = Enum(StatesFederation, index=True)
    country = Column(String, index=True)
    postal_code = Column(String, index=True)

    establishment = relationship("Establishment", back_populates="address")
    user = relationship("User", back_populates="address")
