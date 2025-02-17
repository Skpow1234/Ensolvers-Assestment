from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    notes = relationship("Note", secondary="note_tags", back_populates="tags")
