import os.path
import shutil

from .logger import setup_logger

logger = setup_logger()

class Directory:
    def __init__(self, path):
        self.path = path

    def create_if_not_exists(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            logger.info(f"DIR[{self.path}] tạo thành công")
        else:
            logger.info(f"DIR[{self.path}] đã tồn tại")

    def remove_directory(self):
        try:
            shutil.rmtree(self.path)
        except Exception as e:
            print(e)

    def get_path_files(self):
        return [os.path.join(self.path, i) for i in os.listdir(self.path)]

