from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.note_service import NoteService
from repositories.note_repository import NoteRepository

router = APIRouter()


@router.post("/notes", response_model=dict)
def create_note(title: str, content: str, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    service = NoteService(repository)
    return service.create_note(title, content)


@router.get("/notes", response_model=list)
def list_notes(archived: bool = False, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    service = NoteService(repository)
    return service.list_notes(archived)


@router.get("/notes/{note_id}", response_model=dict)
def get_note(note_id: int, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    service = NoteService(repository)
    note = repository.get_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/notes/{note_id}", response_model=dict)
def update_note(note_id: int, title: str, content: str, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    service = NoteService(repository)
    updated_note = service.update_note(note_id, title, content)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note


@router.delete("/notes/{note_id}", response_model=dict)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    service = NoteService(repository)
    deleted_note = service.delete_note(note_id)
    if not deleted_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted successfully"}


@router.post("/notes/{note_id}/archive", response_model=dict)
def archive_note(note_id: int, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    service = NoteService(repository)
    return service.archive_note(note_id)


@router.post("/notes/{note_id}/unarchive", response_model=dict)
def unarchive_note(note_id: int, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    service = NoteService(repository)
    return service.unarchive_note(note_id)


@router.post("/notes/{note_id}/tags/{tag_id}", response_model=dict)
def add_tag_to_note(note_id: int, tag_id: int, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    return repository.add_tag(note_id, tag_id)


@router.delete("/notes/{note_id}/tags/{tag_id}", response_model=dict)
def remove_tag_from_note(note_id: int, tag_id: int, db: Session = Depends(get_db)):
    repository = NoteRepository(db)
    return repository.remove_tag(note_id, tag_id)
