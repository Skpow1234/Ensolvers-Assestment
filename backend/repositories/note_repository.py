from sqlalchemy.orm import Session
from models.note_model import Note

class NoteRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, content: str):
        note = Note(title=title, content=content)
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)
        return note

    def get_all(self, archived: bool):
        return self.db.query(Note).filter(Note.archived == archived).all()

    def update(self, note_id: int, title: str = None, content: str = None):
        note = self.db.query(Note).get(note_id)
        if title:
            note.title = title
        if content:
            note.content = content
        self.db.commit()
        self.db.refresh(note)
        return note

    def delete(self, note_id: int):
        note = self.db.query(Note).get(note_id)
        self.db.delete(note)
        self.db.commit()
        return note
    
def add_tag(self, note_id: int, tag_id: int):
    note = self.db.query(Note).get(note_id)
    tag = self.db.query(Tag).get(tag_id)
    note.tags.append(tag)
    self.db.commit()
    return note

def remove_tag(self, note_id: int, tag_id: int):
    note = self.db.query(Note).get(note_id)
    tag = self.db.query(Tag).get(tag_id)
    note.tags.remove(tag)
    self.db.commit()
    return note
