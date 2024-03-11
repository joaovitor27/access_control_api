from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.database.database import Base


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    code = Column(String, index=True, unique=True)
    description = Column(String, nullable=True)
    type = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    owner = relationship("User", back_populates="tag")
