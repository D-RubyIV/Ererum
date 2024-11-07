from typing import List, Type

from .. import TgRepository
from ..baseservice import BaseService
from ...equipment.models import TgRecord


class TgService(BaseService):
    def __init__(self):
        self.repo = TgRepository
        self.entity = TgRecord
        super().__init__(self.repo, self.entity)

    def get_all(self) -> List[TgRecord]:
        return super().get_all()