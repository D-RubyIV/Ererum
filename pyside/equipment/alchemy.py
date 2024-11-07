from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

# Tạo engine kết nối với cơ sở dữ liệu
engine = create_engine(f"sqlite+pysqlite:///{settings.DBPATH}", echo=True)
print(f"DB: ", settings.DBPATH)

# Cấu hình session với các thuộc tính
SessionLocal = sessionmaker(
    autocommit=False,   # Không tự động commit
    autoflush=True,     # Tự động flush thay đổi vào DB trước khi thực hiện truy vấn
    bind=engine         # Gắn kết session với engine đã tạo
)

# Hàm để tạo session
def get_session():
    db = SessionLocal()  # Tạo một phiên làm việc (session) mới
    try:
        yield db  # Trả về session để thao tác với cơ sở dữ liệu
    finally:
        db.close()  # Đảm bảo đóng session sau khi sử dụng
