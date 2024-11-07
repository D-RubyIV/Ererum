from sqlalchemy.orm import sessionmaker
from typing import Type, TypeVar, List, Generic

from ..equipment.alchemy import SessionLocal
from ..equipment.models import BaseModel

# Type variable to represent any SQLAlchemy model
T = TypeVar('T', bound=BaseModel)

class BaseRepository(Generic[T]):
    def __init__(self, domain: Type[T]):
        self.domain = domain
        self.session = SessionLocal()

    def add(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        return entity

    def get(self, entity_id: int) -> T:
        return self.session.query(self.domain).filter_by(id=entity_id).first()

    def get_all(self) -> List[T]:
        return self.session.query(self.domain).all()

    def update(self, entity: T) -> T:
        self.session.commit()
        return entity

    def delete(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.commit()
