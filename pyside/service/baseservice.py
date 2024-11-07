from typing import TypeVar, Generic, Type, List

from ..equipment.models import BaseModel
from ..repository.baserepository import BaseRepository

R = TypeVar("R", bound=BaseRepository)
T = TypeVar("T", bound=BaseModel)

class BaseService(Generic[R, T]):
    def __init__(self, repo: Type[R], entity: Type[T]):
        self.repo = repo()
        self.entity = entity()

    def get_repo(self):
        return self.repo

    def get_entity(self) -> T:
        return self.entity

    def get_all(self) -> List[T]:
        return self.repo.get_all()

    def update(self) -> T:
        return self.repo.update(self.entity)

    def delete(self):
        return self.repo.delete(self.entity)

