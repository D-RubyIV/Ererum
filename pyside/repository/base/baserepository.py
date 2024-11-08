from sqlalchemy import update
from sqlalchemy.orm import sessionmaker, Session
from typing import Type, TypeVar, List, Generic, Any

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

    def update_field_for_all(self, field_name: str, new_value: Any) -> None:
        """
        Cập nhật giá trị của một trường cho toàn bộ bản ghi của model.
        :param field_name: Tên của cột cần cập nhật.
        :param new_value: Giá trị mới sẽ được đặt cho cột.
        """
        session = self.get_session()
        field = getattr(self.domain, field_name)
        session.execute(
            update(self.domain).values({field: new_value})
        )
        session.commit()