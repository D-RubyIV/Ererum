from sqlalchemy.orm import sessionmaker

from .baserepository import BaseRepository
from ..equipment.models import TgRecord


class TgRepository(BaseRepository):
    def __init__(self):
        super().__init__(domain=TgRecord)

    def delete_by_id(self, user_id: int) -> None:
        user = self.get(user_id)
        if user:
            self.delete(user)
