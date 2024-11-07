from sqlalchemy.orm import sessionmaker, Session
from typing import Type, TypeVar, List, Generic

from equipment.alchemy import SessionLocal
from equipment.models import BaseModel

# Type variable to represent any SQLAlchemy model
T = TypeVar('T', bound=BaseModel)

class BaseRepository(Generic[T]):
    def __init__(self, domain: Type[T]):
        self.domain = domain
        self.active = SessionLocal()

    def get_session(self) -> Session:
        return self.active

    def add(self, entity: T) -> T:
        self.get_session().add(entity)
        self.get_session().commit()
        return entity

    def get(self, entity_id: int) -> T:
        return self.get_session().query(self.domain).filter_by(id=entity_id).first()

    def get_all(self) -> List[T]:
        return self.get_session().query(self.domain).all()

    def update(self, entity: T) -> T:
        self.get_session().commit()
        return entity

    def delete(self, entity: T) -> None:
        self.get_session().delete(entity)
        self.get_session().commit()

    def update_all(self, entities: List[T]) -> List[T]:
        session = self.get_session()
        for entity in entities:
            session.merge(entity)
        session.commit()
        return entities