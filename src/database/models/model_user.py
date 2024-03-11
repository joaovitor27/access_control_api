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
    tag_id = Column(Integer, ForeignKey("tags.id"))
    establishment_id = Column(Integer, ForeignKey("establishment.id"))

    tag = relationship("Tag", back_populates="owner")
    establishment = relationship("Establishment", back_populates="owner")
