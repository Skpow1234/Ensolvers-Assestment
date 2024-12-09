from repositories.tag_repository import TagRepository

class TagService:
    def __init__(self, repository: TagRepository):
        self.repository = repository

    def create_tag(self, name: str):
        return self.repository.create(name)

    def list_tags(self):
        return self.repository.get_all()
