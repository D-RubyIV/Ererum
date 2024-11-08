from typing import TypeVar, Generic, Type, List, Any

from equipment.models import BaseModel
from repository.base.baserepository import BaseRepository

R = TypeVar("R", bound=BaseRepository)
T = TypeVar("T", bound=BaseModel)

class BaseService(Generic[R, T]):
    def __init__(self, repo: Type[R], entity: Type[T]):
        self.repo = repo()
        self.entity = entity()

    def get_repo(self):
        return self.repo

    def get_session(self):
        return self.repo.get_session()

    def get_entity(self) -> T:
        return self.entity

    def get_all(self) -> List[T]:
        return self.repo.get_all()

    def update(self) -> T:
        return self.repo.update(self.entity)

    def delete(self):
        return self.repo.delete(self.entity)

    def commit(self):
        self.repo.get_session().commit()

    def update_field_for_all(self, field_name: str, new_value: Any) -> None:
        self.repo.update_field_for_all(field_name, new_value)
