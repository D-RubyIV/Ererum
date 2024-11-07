import os.path
from typing import List

from service.base.baseservice import  BaseService
from equipment.alchemy import SessionLocal
from equipment.models import TgRecord
from repository.tg.tgrepositoy import TgRepository


class TgService(BaseService):
    def __init__(self):
        self.repo = TgRepository
        self.entity = TgRecord
        self.sessionLocal = SessionLocal
        super().__init__(self.repo, self.entity)

    def get_all(self) -> List[TgRecord]:
        return super().get_all()

    def sync_local(self, tg_file_paths):
        session = self.sessionLocal()
        file_names = [os.path.basename(path) for path in tg_file_paths if os.path.basename(path).endswith(".session")]
        existing_names = {name for name, in session.query(TgRecord.name).all()}

        from datetime import datetime

        now = datetime.now()
        new_files = [{"name": name, "created_time": now, "updated_time": now} for name in file_names if name not in existing_names]

        if new_files:
            session.bulk_insert_mappings(TgRecord, new_files)
            session.commit()

        session.close()

    def get_all_in_list_name(self, file_names)-> List[TgRecord]:
        return super().get_repo().get_all_in_list_name(file_names=file_names)




