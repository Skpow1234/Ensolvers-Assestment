from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.tag_service import TagService
from repositories.tag_repository import TagRepository

router = APIRouter()


@router.post("/tags", response_model=dict)
def create_tag(name: str, db: Session = Depends(get_db)):
    repository = TagRepository(db)
    service = TagService(repository)
    existing_tag = repository.get_by_name(name)
    if existing_tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    return service.create_tag(name)


@router.get("/tags", response_model=list)
def list_tags(db: Session = Depends(get_db)):
    repository = TagRepository(db)
    service = TagService(repository)
    return service.list_tags()


@router.get("/tags/{tag_id}", response_model=dict)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    repository = TagRepository(db)
    tag = repository.get_by_id(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.delete("/tags/{tag_id}", response_model=dict)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    repository = TagRepository(db)
    tag = repository.get_by_id(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    repository.delete(tag_id)
    return {"detail": "Tag deleted successfully"}
