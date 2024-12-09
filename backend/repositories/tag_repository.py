from sqlalchemy.orm import Session
from models.tag_model import Tag

class TagRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str):
        tag = Tag(name=name)
        self.db.add(tag)
        self.db.commit()
        self.db.refresh(tag)
        return tag

    def get_all(self):
        return self.db.query(Tag).all()

    def get_by_name(self, name: str):
        return self.db.query(Tag).filter_by(name=name).first()
