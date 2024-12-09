from repositories.note_repository import NoteRepository

class NoteService:
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    def create_note(self, title: str, content: str):
        return self.repository.create(title, content)

    def list_notes(self, archived: bool = False):
        return self.repository.get_all(archived)

    def update_note(self, note_id: int, title: str = None, content: str = None):
        return self.repository.update(note_id, title, content)

    def delete_note(self, note_id: int):
        return self.repository.delete(note_id)
