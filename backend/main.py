from fastapi import FastAPI
from routes.note_routes import router as note_router
from routes.tag_routes import router as tag_router
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(note_router, prefix="/api")
app.include_router(tag_router, prefix="/api")
