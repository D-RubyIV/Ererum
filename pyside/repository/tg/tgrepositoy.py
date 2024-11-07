from repository.base.baserepository import BaseRepository
from equipment.models import TgRecord


class TgRepository(BaseRepository):
    def __init__(self):
        super().__init__(domain=TgRecord)

    def delete_by_id(self, user_id: int) -> None:
        user = self.get(user_id)
        if user:
            self.delete(user)

    def get_all_in_list_name(self, file_names):
        records = super().get_session().query(TgRecord).filter(TgRecord.name.in_(file_names))
        return records


